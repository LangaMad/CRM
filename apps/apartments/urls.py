from django.urls import path,include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register("apartments",ApartmentViewSet)

urlpatterns = [
    path('',include(router.urls))
]