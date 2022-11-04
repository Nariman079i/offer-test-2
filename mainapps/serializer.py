from rest_framework.serializers import *
from mainapps.models import *


class ApplicationSerializer(ModelSerializer):

    class Meta:
        model = Application
        fields = '__all__'


class RoleSerializer(ModelSerializer):

    class Meta:
        model = Role
        fields = '__all__'
