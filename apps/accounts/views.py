from django.shortcuts import render
from rest_framework.generics import *
from .serializers import ManagerSerializer
from rest_framework.viewsets import *

from .models import *
# Create your views here.

class ManagerViewSet(ModelViewSet):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer





