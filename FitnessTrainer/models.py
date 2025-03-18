from django.db import models
from Guest.models import *

# Create your models here.

class Package(models.Model):
    package_name=models.CharField(max_length=111)
    package_details=models.CharField(max_length=111)
    package_duration=models.CharField(max_length=111)
    package_fees=models.CharField(max_length=111)
    fitnesstrainer_id=models.ForeignKey(FitnessTrainer,on_delete=models.SET_NULL,null=True)
    yogatrainer_id=models.ForeignKey(YogaTrainer,on_delete=models.SET_NULL,null=True)
    zumbatrainer_id=models.ForeignKey(ZumbaTrainer,on_delete=models.SET_NULL,null=True)
    package_photo=models.FileField(upload_to='tpackagedocs/')



class Course(models.Model):
    package=models.ForeignKey(Package,on_delete=models.SET_NULL,null=True)
    course_details=models.TextField(null=True)
    course_video=models.FileField(upload_to='course_videos/')
    course_day=models.CharField(max_length=50)
    uploaded_date=models.DateField(auto_now=True)
    c_status=models.IntegerField(default=0)
    
    
    

    



