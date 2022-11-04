from django.urls import path , include
from mainapps.views import *
from rest_framework.routers import *

# router = DefaultRouter()
# router.register(r'main', ApplicationModelSet , basename='application')
# print(router.urls)
urlpatterns = [
    # path('', include(router.urls)),
    path('apps/create/', ApplicationAPIViewCreate.as_view()),
    path('apps/', ApplicationAPIViewList.as_view()),
]