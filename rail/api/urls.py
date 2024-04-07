from django.conf.urls import url
from django.urls import path,include
from .views import *
from rest_framework import routers
router=routers.DefaultRouter()
router.register(r'trains',TrainsAPIView)
router.register(r'route',RouteAPIView)
router.register(r'station',StationAPIView)

router.register(r'routeStation',RouteStationAPIView)
router.register(r'reservation',ReservationAPIView)
# router.register(r'register_user',CreateAccountAPIView)
router.register(r'account',AccountListAPIView)
router.register(r'payment',PaymentAPIView)
# router.register(r'route',RouteAPIView)

urlpatterns = [
    path('',include(router.urls))
    # url(r'^trains',TrainsAPIView.as_view(),name='trains'),
    # url(r'^route/',RouteAPIView.as_view(),name='route'),

]
