from rest_framework import serializers
from .models import Users

# Se realiza la serialización de cada uno de los objetos para mostrarlos en formato json y legibles de manera clara


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
