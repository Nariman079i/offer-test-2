from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.generics import *
from rest_framework import mixins
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet, GenericViewSet
from dadata import Dadata
from api.models import Object, Category
from json import *
# Create your views here.
from api.serializers import ObjectSerializer


def get_inn_user(request, inn):
    token = "d4cbcec638775b2531d59feab5387d70c32d420b"
    dadata = Dadata(token)
    file = 'api/index.html'
    result = dadata.find_by_id("party", inn)
    if len(result) <= 0:
        data = "Taкого ИНН не существует"

    else:


        data = dumps(result, indent=4 , ensure_ascii=False)

    return HttpResponse(dumps(result , indent=4 , ensure_ascii=False , sort_keys=False, separators=(',' , ':')), content_type="application/json")


class ObjectReadAndEditView(mixins.ListModelMixin,
                            mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            GenericViewSet):
    queryset = Object.objects.all()
    serializer_class = ObjectSerializer


class ObjectSetView(ModelViewSet):
    queryset = Object.objects.all()
    serializer_class = ObjectSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            return Object.objects.all()
        return Object.objects.filter(pk=pk)

    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        cats = Category.objects.get(pk=pk)
        return Response({'cats': cats.title})

    # @action(method=['get'], detail=False)


class ObjectReadOnlyViewSet(ReadOnlyModelViewSet):
    queryset = Object.objects.all()
    serializer_class = ObjectSerializer
# class ObjectApiList(ListAPIView):
#     queryset = Object.objects.all()
#     serializer_class = ObjectSerializer
#
#
# class ObjectApiListCreate(ListCreateAPIView):
#     queryset = Object.objects.all()
#     serializer_class = ObjectSerializer
#
#
# class ObjectApiDetailViewCRUD(RetrieveUpdateDestroyAPIView):
#     queryset = Object.objects.all()
#     serializer_class = ObjectSerializer
#
#
# class ObjectApiDetailView(RetrieveAPIView):
#     queryset = Object.objects.all()
#     serializer_class = ObjectSerializer
#
# class ObjectApiDetailUpdateView(RetrieveUpdateAPIView):
#     queryset = Object.objects.all()
#     serializer_class = ObjectSerializer
