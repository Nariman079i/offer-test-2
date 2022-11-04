from django.urls import path , include
from rest_framework.routers import SimpleRouter, DefaultRouter
from testapp.views import *
from rest_framework.routers import *


router = DefaultRouter()
router.register(r'profile', ProfileAllApiView, basename="profile")
print(router.urls)
urlpatterns = [
    # path('', ProfileApiList.as_view()),
    # path('create/', ProfileApiCreate.as_view())
    path('',include(router.urls))
]
