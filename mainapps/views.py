from django.shortcuts import render, HttpResponse
from rest_framework.decorators import action
from rest_framework.generics import *
from rest_framework.permissions import *
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from mainapps.serializer import *
from mainapps.models import *



# class ApplicationModelSet(mixins.ListModelMixin , mixins.RetrieveModelMixin, GenericViewSet):
#
#     def get_queryset(self):
#         pk = self.kwargs.get('pk')
#         if not pk:
#             return Application.objects.all()
#         return Application.objects.filter(pk=pk)
#
#     serializer_class = ApplicationSerializer
#     @action(methods=['get'] , detail=True)
#     def role(self,request, pk=None):
#         roles = Role.objects.get(pk=pk)
#         return Response({'role': roles.title})
#







#def index(request):
#   return HttpResponse('<h1>Main page</h1>')
class ApplicationAPIViewList(ListAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = (AllowAny,)

class ApplicationAPIViewCreate(ListCreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

