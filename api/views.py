# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Book
from .seriallzers import BookSeriallzer


class TestView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            'message': '我是message'
        }
        return Response(data=data)


class BookView(APIView):

    def get(self, request):
        res = Book.get_python_books()
        print(res)
        book_list = Book.objects.all()
        ret = BookSeriallzer(book_list, many=True)  # 序列化过程
        return Response(ret.data)

    def post(self, request):
        print("数据", request.data)
        serializer = BookSeriallzer(data=request.data)  # 反序列化
        if serializer.is_valid():
            print("验证通过")
            serializer.save()  # save()方法保存数据库，需要在序列化器里自定义create方法
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def put(self, request, book_id):
        print(book_id)
        print("数据", request.data)
        instance = Book.objects.filter(id=int(book_id)).first()
        serializer = BookSeriallzer(instance=instance, data=request.data)  # 反序列化
        if serializer.is_valid():

            # print(serializer.validated_data.get('title'))
            print(type(instance))
            print("验证通过")
            serializer.save()  # save()方法保存数据库，需要在序列化器里自定义update方法
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        # return Response({'msg': 1})

    def patch(self, request, book_id):
        print(book_id)
        print("数据", request.data)
        instance = Book.objects.filter(id=int(book_id)).first()
        # 允许部分提交数据  不会触发未提交字段必填的异常  用来做patch请求非常合适
        serializer = BookSeriallzer(instance=instance, data=request.data, partial=True)  # 反序列化
        if serializer.is_valid():

            # print(serializer.validated_data.get('title'))
            print(type(instance))
            print("验证通过")
            serializer.save()  # save()方法保存数据库，需要在序列化器里自定义update方法
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        # return Response({'msg': 1})

    def delete(self, request, book_id):
        instance = Book.objects.filter(id=book_id).first()
        instance.delete()
        return Response({'msg': 1})
