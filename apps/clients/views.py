from rest_framework.generics import *
from .serializers import ClientSerializer
from rest_framework.viewsets import *
from .models import *
# Create your views here.

class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer






