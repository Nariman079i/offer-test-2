from leveone.serializers import *
from rest_framework.generics import *
from rest_framework.permissions import *
from leveone.models import *



class CategoryApiCreate(CreateAPIView, ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    permission_classes = (IsAuthenticatedOrReadOnly,)


class ProductApiList(ListAPIView,CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    permission_classes = (IsAuthenticatedOrReadOnly,)

