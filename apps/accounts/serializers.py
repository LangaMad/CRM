from rest_framework import serializers
from .models import Manager

class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = ['id','full_name', 'phone_number', 'email', 'number_of_deals']
        read_only_fields = ["id",'number_of_deals','created_at']