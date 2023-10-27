from rest_framework import serializers
from .models import Categ

class CategSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categ
        fields = '__all__'