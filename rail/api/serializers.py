from rest_framework import serializers
from django.contrib.auth import get_user_model # If used custom user model

UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = UserModel.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )

        return user

    class Meta:
        model = UserModel
        # Tuple of serialized model fields (see link [2])
        fields = ( "id", "username", "password", )

from .models import *
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Client
        fields=('__all__')

class CleinSerializer(serializers.ModelSerializer):
    class Meta:
        model=Clein
        fields=('__all__')

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model=Account
        fields=('__all__')
class TrainsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Trains
        fields=('__all__')


class RouteSerializers(serializers.ModelSerializer):
    class Meta:
        model=Route
        fields=('__all__')
        
class StationSerializers(serializers.ModelSerializer):
    class Meta:
        model=Station
        fields=('__all__')

class RouteStationSerializers(serializers.ModelSerializer):
    class Meta:
        model=RouteStation
        fields=('__all__')
        
class ReservationSerializers(serializers.ModelSerializer):
    class Meta:
        model=Reservation
        fields=('__all__')
        
class PaymentSerializers(serializers.ModelSerializer):
    class Meta:
        model=Payment
        fields=('__all__')
        
