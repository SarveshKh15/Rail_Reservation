from django.contrib import admin
# Register your models here.
from .models import *
from django.contrib.auth.admin import UserAdmin
class UserModel(UserAdmin):
    list_display=['username','user_type']
admin.site.register(CustomUser,UserModel)
admin.site.register(Trains)
admin.site.register(Route)
# admin.site.register(Client)
admin.site.register(Station)
admin.site.register(RouteStation)

admin.site.register(Reservation)
admin.site.register(Payment)
admin.site.register(Account)
admin.site.register(Clein)