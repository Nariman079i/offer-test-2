from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.generics import *
from rest_framework.permissions import *
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from testapp.models import Profile
from testapp.permissions import IsAdminOrReadOnly
from testapp.serializers import *


class ProfileAllApiView(ModelViewSet):
    serializer_class = ProfileSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            return Profile.objects.all()
        return Profile.objects.filter(pk=pk)

    @action(methods=['get', ], detail=False)
    def role(self, request):
        # if pk is None:
        role = Role.objects.all()
        return Response({'roles':[r.title for r in role]})

        # role = Role.objects.get(pk=pk)
        # return Response({'role':role.title})

    permission_classes = (IsAdminOrReadOnly,)


class ProfileApiList(ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileApiCreate(CreateAPIView):

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    @action(methods=['get', ],detail=False)
    def role(self):
        return Role.objects.all()

    permission_classes = (IsAdminUser,)

