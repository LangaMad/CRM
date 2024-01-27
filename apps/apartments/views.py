from rest_framework.generics import *
from .serializers import ApartmentSerializer
from rest_framework.viewsets import *
from .models import *
# Create your views here.

class ApartmentViewSet(ModelViewSet):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
    def perform_create(self, serializer):
        instance = serializer.save()

        if instance.manager:
            instance.manager.number_of_deals += 1
            instance.manager.save()


