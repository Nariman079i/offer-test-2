from django.urls import path , include
from rest_framework.routers import SimpleRouter, DefaultRouter
from api.views import *
from api.views import *

router = DefaultRouter()
router.register(r'object', ObjectSetView, basename='object')
router.register(r'read-object', ObjectReadOnlyViewSet)
router.register(r'read-edit-object', ObjectReadAndEditView)



urlpatterns = [
    # path('object/<str:name>/', ObjectApiDetailView.as_view()),
    # path('objects/',  ObjectApiListCreate.as_view() )
    path('v1/', include(router.urls)),
    path('inn/<str:inn>/', get_inn_user)

    # path('object/', ObjectSetView.as_view({'get':'list'})),
    # path('object/<int:pk>/', ObjectSetView.as_view({'get': 'retrieve'})),
    # path('object/edit/<int:pk>/', ObjectSetView.as_view({'put': 'update'}))
]
