from django.db import models
from Admin.models import Place,Subtype

# Create your models here.

class URegistration(models.Model):
    user_name=models.CharField(max_length=100)
    user_contact=models.CharField(max_length=100)
    user_email=models.EmailField(unique=True)
    user_gender=models.CharField(max_length=100)
    user_age=models.CharField(max_length=100)
    user_address=models.TextField(null=True)
    user_photo=models.FileField(upload_to='userdocs/')
    user_proof=models.FileField(upload_to='userdocs/')
    user_password=models.CharField(max_length=100,unique=True)
    place_id=models.ForeignKey(Place,on_delete=models.CASCADE)
    user_doj=models.DateField(auto_now=True)
    user_vstatus=models.IntegerField(default=0)


class FitnessTrainer(models.Model):
    fitness_name=models.CharField(max_length=100)
    fitness_contact=models.CharField(max_length=100)
    fitness_email=models.EmailField(unique=True)
    fitness_address=models.TextField(null=True)
    fitness_qualification=models.TextField(null=True)
    fitness_certificate=models.FileField(upload_to='fitnessdocs/')
    fitness_photo=models.FileField(upload_to='fitnessdocs/')
    fitness_password=models.CharField(max_length=100)
    subtype=models.ForeignKey(Subtype,on_delete=models.SET_NULL,null=True)
    place_id=models.ForeignKey(Place,on_delete=models.CASCADE)
    fitness_vstatus=models.IntegerField(default=0)


class YogaTrainer(models.Model):
    yoga_name=models.CharField(max_length=100)
    yoga_contact=models.CharField(max_length=100)
    yoga_email=models.EmailField(unique=True)
    yoga_address=models.TextField(null=True)
    yoga_qualification=models.TextField(null=True)
    yoga_certificate=models.FileField(upload_to='fitnessdocs/')
    yoga_photo=models.FileField(upload_to='fitnessdocs/')
    yoga_password=models.CharField(max_length=100)
    subtype=models.ForeignKey(Subtype,on_delete=models.SET_NULL,null=True)
    place_id=models.ForeignKey(Place,on_delete=models.CASCADE)
    yoga_vstatus=models.IntegerField(default=0)


class ZumbaTrainer(models.Model):
    zumba_name=models.CharField(max_length=100)
    zumba_contact=models.CharField(max_length=111)
    zumba_email=models.EmailField(unique=True)
    zumba_address=models.TextField(null=True)
    zumba_qualification=models.TextField(null=True)
    zumba_certificate=models.FileField(upload_to='fitnessdocs/')
    zumba_photo=models.FileField(upload_to='fitnessdocs/')
    zumba_password=models.CharField(max_length=100)
    subtype=models.ForeignKey(Subtype,on_delete=models.SET_NULL,null=True)
    place_id=models.ForeignKey(Place,on_delete=models.CASCADE)
    zumba_vstatus=models.IntegerField(default=0)