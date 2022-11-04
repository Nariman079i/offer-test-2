from django.urls import path, include, re_path
from leveone.views import *


urlpatterns = [
    path('', ProductApiList.as_view()),
    path('cat/', CategoryApiCreate.as_view()),
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken'))
]