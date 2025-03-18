from django.db import models
from Guest.models import *
from Admin.models import *
from FitnessTrainer.models import Package
# Create your models here.

class Booking(models.Model):
    user=models.ForeignKey(URegistration,on_delete=models.SET_NULL,null=True)
    booking_status=models.IntegerField(default=0)
    booking_date=models.DateField(auto_now=True)

class Cart(models.Model):
    booking=models.ForeignKey(Booking,on_delete=models.SET_NULL,null=True)
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    cart_quantity=models.IntegerField(default=1)



class BookPackage(models.Model):
    package=models.ForeignKey(Package,on_delete=models.SET_NULL,null=True)
    user=models.ForeignKey(URegistration,on_delete=models.SET_NULL,null=True)
    booking_date=models.DateField(auto_now=True)
    booking_status=models.IntegerField(default=0)
    payment_status=models.IntegerField(default=0)




class Chat(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    from_user = models.ForeignKey(
        URegistration, on_delete=models.SET_NULL, default=False, null=True, related_name="from_usr")
    to_user = models.ForeignKey(
        URegistration, on_delete=models.SET_NULL, default=False, null=True, related_name="to_usr")
    from_fitness = models.ForeignKey(
        FitnessTrainer, on_delete=models.SET_NULL, default=False, null=True, related_name="from_fitnss")
    to_fitness = models.ForeignKey(
        FitnessTrainer, on_delete=models.SET_NULL, default=False, null=True, related_name="to_fitnss")
    content = models.TextField()
    
    
    
    
class Complaint(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField(null=True)
    date=models.DateField(auto_now=True)
    reply=models.TextField(null=True)
    c_status=models.IntegerField(default=0)
    user=models.ForeignKey(URegistration,on_delete=models.SET_NULL,null=True)
    fitnesstrainer_id=models.ForeignKey(FitnessTrainer,on_delete=models.SET_NULL,null=True)
    yogatrainer_id=models.ForeignKey(YogaTrainer,on_delete=models.SET_NULL,null=True)
    zumbatrainer_id=models.ForeignKey(ZumbaTrainer,on_delete=models.SET_NULL,null=True)
    

class Feedback(models.Model):
    description=models.TextField(null=True)
    date=models.DateField(auto_now=True)
    user=models.ForeignKey(URegistration,on_delete=models.SET_NULL,null=True)
    fitnesstrainer_id=models.ForeignKey(FitnessTrainer,on_delete=models.SET_NULL,null=True)
    yogatrainer_id=models.ForeignKey(YogaTrainer,on_delete=models.SET_NULL,null=True)
    zumbatrainer_id=models.ForeignKey(ZumbaTrainer,on_delete=models.SET_NULL,null=True)