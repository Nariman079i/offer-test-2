from rest_framework.serializers import HiddenField , ModelSerializer, CurrentUserDefault
from testapp.models import *


class ProfileSerializer(ModelSerializer):

    user = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Profile
        fields = "__all__"