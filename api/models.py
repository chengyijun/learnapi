from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=32, verbose_name="图书名称")
    CHOICES = ((1, "Python"), (2, "Go"), (3, "Linux"))
    category = models.IntegerField(choices=CHOICES, verbose_name="图书的类别")
    pub_time = models.DateField(verbose_name="图书的出版日期")

    # 外键关系
    """
    给on_delete关键字给定以下参数中的一个：
    　　models.CASCADE：级联删除。当删除'一'时，‘多’会被删除。
    　　modles.PROTECT: 当删除一个具有外键关系的对象时，会引发一个异常，阻止删除该对象
    　　models.SET_NULL:设置删除对象所关联的外键字段为null。但字段的null属性必需为True
    　　models.SET_DEFAULT:设置删除对象所关联的外键字段为默认的值。
    　　models.SET(value)：设置删除对象所关联的对象的外键字段为value,value也可以是一个可调用函数。
    　　models.DO_NOTHING: 不做任何操作
    """
    publisher = models.ForeignKey(to="Publisher", on_delete=models.CASCADE)
    # 多对多关系
    author = models.ManyToManyField(to="Author")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Book"
        db_table = verbose_name_plural

    @classmethod
    def get_python_books(cls):
        return cls.objects.filter(author__book__title__contains="linux")


class Publisher(models.Model):
    title = models.CharField(max_length=32, verbose_name="出版社的名称")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Publisher"
        db_table = verbose_name_plural


class Author(models.Model):
    name = models.CharField(max_length=32, verbose_name="作者的姓名")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Author"
        db_table = verbose_name_plural
