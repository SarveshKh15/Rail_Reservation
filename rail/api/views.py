from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from rest_framework import generics,status,viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.decorators import action
from rest_framework.response import Response
class TrainsAPIView(viewsets.ModelViewSet):
    queryset=Trains.objects.all()
    serializer_class=TrainsSerializer
    
class RouteAPIView(viewsets.ModelViewSet):
    queryset=Trains.objects.all()
    serializer_class=RouteSerializers

class RouteStationAPIView(viewsets.ModelViewSet):
    queryset=Trains.objects.all()
    serializer_class=RouteStationSerializers
    
class StationAPIView(viewsets.ModelViewSet):
    queryset=Trains.objects.all()
    serializer_class=StationSerializers

class ReservationAPIView(viewsets.ModelViewSet):
    queryset=Trains.objects.all()
    serializer_class=ReservationSerializers
    
class PaymentAPIView(viewsets.ModelViewSet):
    queryset=Trains.objects.all()
    serializer_class=PaymentSerializers

class CreateAccountAPIView(APIView):
    def post(self,request):
        """
        {
            "full_name":"sarvesh khandare",
            "address":"Nagpur"
            
            
        }
        """
       
        client=Clein.objects.create(
            name=request.data['full_name'],
            address=request.data['address'],
        )
        account=Account.objects.create(
            client=client,
        )
        serializer=AccountSerializer(account)
        return Response(serializer.data)
        # pass
        
class AccountListAPIView(viewsets.ModelViewSet):
    queryset=Account.objects.all()
    serializer_class=AccountSerializer