from django.db import models

# Create your models here.

class Admin(models.Model):
    admin_name=models.CharField(max_length=100)
    admin_email=models.CharField(max_length=100)
    admin_password=models.CharField(max_length=100)


class TrainerType(models.Model):
    ttype_name=models.CharField(max_length=100)

    def __str__(self):
        return self.ttype_name

class Subtype(models.Model):
    subtype_name=models.CharField(max_length=50)
    ttype=models.ForeignKey(TrainerType,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.subtype_name


class ProductType(models.Model):
    ptype_name=models.CharField(max_length=100)

class District(models.Model):
    district_name=models.CharField(max_length=50)

    def __str__(self):
        return self.district_name

class Place(models.Model):
    place_name=models.CharField(max_length=100)
    pincode=models.CharField(max_length=50)
    district=models.ForeignKey(District,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.place_name

class Product(models.Model):
    product_name=models.CharField(max_length=100)
    product_image=models.FileField(upload_to='productdocs/')
    product_details=models.CharField(max_length=100)
    product_rate=models.CharField(max_length=100)
    product_brand=models.CharField(max_length=100)

class Stock(models.Model):
    stock_date=models.DateField(auto_now=True)
    stock_quantity=models.CharField(max_length=111)
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)

