from rest_framework.serializers import *
from api.models import *

class ObjectSerializer(ModelSerializer):
    class Meta:
        model = Object
        fields = "__all__"