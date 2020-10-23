# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from api2.models import UserInfo, UserGroup
from api2.seriallzers import UserModelSerializer, GroupSerializer


class TestView(APIView):
    def get(self, request, *args, **kwargs):
        userinfos = UserInfo.objects.all()
        # ser = UserSerializer(instance=userinfos, many=True)
        ser = UserModelSerializer(instance=userinfos, many=True, context={'request': request})
        print(ser)
        # data = {'code': 1, 'msg': 'hello abel'}
        return Response(data=ser.data)


class GroupDetailView(APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('group_id')
        usergroup = UserGroup.objects.filter(pk=pk).first()
        # ser = UserSerializer(instance=userinfos, many=True)
        ser = GroupSerializer(instance=usergroup)
        # print(ser)
        # data = {'code': 1, 'msg': 'hello abel'}
        return Response(data=ser.data)
