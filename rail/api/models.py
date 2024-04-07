from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from django.utils.timezone import now
# Create your models here.
class CustomUser(AbstractUser):
    USER={
       (1,'Client')
        
    }
    user_type=models.CharField(choices=USER,max_length=100,default=1)

class Client(models.Model):
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)
    mobile=models.CharField(max_length=100,default="0")
    dob=models.DateField(default=datetime.now)
    gender=models.CharField(max_length=100,default="male")
    address=models.TextField(default="")
 
    def __str__(self):
        return self.name

class Clein(models.Model):
    name=models.CharField(max_length=100)
    address=models.TextField(default="")
    def __str__(self):
        return self.name
    
class Account(models.Model):
    client=models.ForeignKey(Clein,on_delete=models.CASCADE)


class Station(models.Model):
    # rid=models.ForeignKey(Route,on_delete=models.CASCADE)

    # sid=models.CharField(primary_key=True,max_length=50)
    sname=models.CharField(max_length=50)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)

    def __str__(self):
        return self.sname


class Route(models.Model):
    rid=models.CharField(max_length=50,default="0")
    ostation=models.ForeignKey(Station,related_name='related_p',on_delete=models.CASCADE,null=True)
    dstation=models.ForeignKey(Station,related_name='Dstayon',on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.rid+" "+self.ostation.sname+" to "+self.dstation.sname

class Trains(models.Model):
    seats=models.IntegerField(default=100)
    price=models.IntegerField(default=500)
    tno=models.CharField(primary_key=True,max_length=20,default=0)
    tname=models.CharField(max_length=50,unique=True)
    rid=models.ForeignKey(Route,on_delete=models.CASCADE)

    def __str__(self):
        return self.tname
    



class RouteStation(models.Model):
    rid=models.ForeignKey(Route,on_delete=models.CASCADE)
    tno=models.ForeignKey(Trains,on_delete=models.CASCADE)
    sid=models.ForeignKey(Station,on_delete=models.CASCADE)
    order=models.IntegerField()
    atime=models.CharField(max_length=50)
    def __str__(self):
        return f"{self.sid.sname}  ---stop for ({self.rid.ostation} - {self.rid.dstation} )"
        # return self.sid.sname
class Reservation(models.Model):
    client=models.ForeignKey(Clein,on_delete=models.CASCADE)
    nos=models.IntegerField() 
    date=models.DateField(max_length=50)
    # amt=models.IntegerField()
    cls=models.CharField(max_length=50)
    # status=models.CharField(max_length=50)
    pnr=models.AutoField(primary_key=True)
    source=models.ForeignKey(Station,related_name='related_primary_manual_roat',on_delete=models.CASCADE,null=True)
    destinaton=models.ForeignKey(Station,related_name='related_seconday',on_delete=models.CASCADE,null=True)
    tname=models.ForeignKey(Trains,on_delete=models.CASCADE)
    
    # ans=Route.objects.filter(ostation=source, dstation=destinaton, trains=tname).exists()
    def __str__(self):
        return f"{self.client} {self.pnr}"


class Payment(models.Model):
    pnr=models.CharField(max_length=50)
    user=models.CharField(max_length=50)
    amt=models.IntegerField()
    mtd=models.CharField(max_length=50)
    date=models.CharField(max_length=50)
    cancel=models.CharField(max_length=50)
    