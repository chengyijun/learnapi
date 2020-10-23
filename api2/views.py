# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from api2.models import UserInfo
from api2.seriallzers import UserModelSerializer


class TestView(APIView):
    def get(self, request, *args, **kwargs):
        userinfos = UserInfo.objects.all()
        # ser = UserSerializer(instance=userinfos, many=True)
        ser = UserModelSerializer(instance=userinfos, many=True)
        print(ser)
        # data = {'code': 1, 'msg': 'hello abel'}
        return Response(data=ser.data)
