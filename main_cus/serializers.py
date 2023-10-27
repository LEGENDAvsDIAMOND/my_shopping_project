from rest_framework import serializers
from .models import MainCus

class MainCusSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainCus
        fields = '__all__'