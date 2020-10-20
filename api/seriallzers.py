from rest_framework import serializers

from api.models import Book


class PublishSeriallzer(serializers.Serializer):
    title = serializers.CharField(max_length=32)


class AuthorSeriallzer(serializers.Serializer):
    name = serializers.CharField(max_length=32)


def my_validate(value):
    if "mingan" in value.lower():
        raise serializers.ValidationError("不能含有敏感信息")
    else:
        return value


"""
class BookSeriallzer(serializers.Serializer):
    # 字段校验三种方式
    # validators制定方法验证 > hook方法验证 > 全局验证

    # 读写
    title = serializers.CharField(max_length=32, validators=[my_validate])  # 此种验证方式比局部钩子优先级高
    pub_time = serializers.DateField()

    # 只读
    id = serializers.IntegerField(required=False)  # required False的意思是 反序列化（存库）的时候非必需
    CHOICES = ((1, "Python"), (2, "Go"), (3, "Linux"))
    category = serializers.ChoiceField(choices=CHOICES, source="get_category_display",
                                       read_only=True)  # 只在序列化(读库)的时候起作用
    publisher = PublishSeriallzer(read_only=True)
    author = AuthorSeriallzer(many=True, read_only=True)  # 通过many参数来区别是普通外键还是多对多关系

    # 只写
    w_category = serializers.ChoiceField(choices=CHOICES, write_only=True)  # 只在反序列化的时候用(存库)
    publisher_id = serializers.IntegerField(write_only=True)
    author_list = serializers.ListField(write_only=True)

    class Meta:
        model = Book  # 设置关联模型     model就是关联模型
        # fields = ['id', 'title']

    def create(self, validated_data):
        book = Book.objects.create(title=validated_data["title"], category=validated_data["w_category"],
                                   pub_time=validated_data["pub_time"], publisher_id=validated_data["publisher_id"])
        book.author.add(*validated_data["author_list"])
        return book

    def update(self, instance, validated_data):
        print('我被调用了 更新')
        "instance是views函数中传来的book_obj"
        instance.title = validated_data.get("title", instance.title)  # 如果已验证的数据中没有title字段，不更新，不会报错
        instance.category = validated_data.get("w_category", instance.category)
        instance.pub_time = validated_data.get("pub_time", instance.pub_time)
        instance.publisher_id = validated_data.get("publisher_id", instance.publisher_id)
        if validated_data.get("author_list"):
            instance.author.set(validated_data["author_list"])  # 更新多对多字段
        instance.save()
        return instance

    def validate_title(self, value):
        "局部钩子，自定义对title字段的验证"
        if "python" not in value.lower():
            raise serializers.ValidationError("标题必须含有python")
        return value

    def validate(self, attrs):
        "全局的校验规则，可以进行多字段联合校验"
        if attrs["w_category"] == 1 and attrs["publisher_id"] == 1:
            return attrs
        else:
            raise serializers.ValidationError("分类以及标题不符合要求")
"""


class BookSeriallzer(serializers.ModelSerializer):
    category_display = serializers.SerializerMethodField()  # 读取数据时的字段名（与"category"区分开来，下同）
    publisher_info = serializers.SerializerMethodField()  # 配合 get_字段名() 钩子，自定义通过外键取出的字段
    authors = serializers.SerializerMethodField()

    def get_category_display(self, obj):
        return obj.get_category_display()

    def get_publisher_info(self, obj):
        # obj 是每个book对象
        publisher_obj = obj.publisher
        # return {"id": publisher_obj.id, "title": publisher_obj.title}  # 只取出来自己想要的数据，不会有其他的冗余数据
        return publisher_obj.title

    def get_authors(self, obj):
        authors = obj.author.all()
        # return [{"id": author.id, "name": author.name} for author in authors]
        return [author.name for author in authors]

    class Meta:
        model = Book  # 对应ORM表
        # fields = ["id", "title", "pub_time", "category"] # 需要取出的字段
        fields = "__all__"  # 表示要取出所有字段
        # depth = 1   # 序列化的外键层级。如果不规定此值，所有的外键字段都只是id。有个缺点：会取出外键对应的所有数据，非常冗余
        extra_kwargs = {
            "category": {"write_only": True},  # “category”字段只写
            "publisher": {"write_only": True},
            "author": {"write_only": True}
        }
