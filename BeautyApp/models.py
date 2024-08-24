from django.db import models

# Create your models here.
class CategoryDB(models.Model):
    catg_name = models.CharField(max_length=100, null=True, blank=True)
    catg_desc = models.CharField(max_length=100, null=True, blank=True)
    catg_image = models.ImageField(upload_to="Category Images", null=True, blank=True)

class ServiceDB(models.Model):
    Category = models.CharField(max_length=100, null=True, blank=True)
    Service_name = models.CharField(max_length=100, null=True, blank=True)
    Service_price = models.CharField(max_length=100,null=True, blank=True)
    Service_desc = models.CharField(max_length=100, null=True, blank=True)
    Service_image = models.ImageField(upload_to="Service Images", null=True, blank=True)

class Hairservicedb(models.Model):
    Haircat_name = models.CharField(max_length=100, null=True, blank=True)
    Hair_category = models.CharField(max_length=100, null=True, blank=True)
    Hair_name = models.CharField(max_length=100, null=True, blank=True)
    Hair_price = models.CharField(max_length=100, null=True, blank=True)
    Hair_desc = models.CharField(max_length=100, null=True, blank=True)
    Hair_image = models.ImageField(upload_to="Hair Images", null=True, blank=True)

class Skinservicedb(models.Model):
    Skincat_name = models.CharField(max_length=100, null=True, blank=True)
    Skin_category = models.CharField(max_length=100, null=True, blank=True)
    Skin_name = models.CharField(max_length=100, null=True, blank=True)
    Skin_price = models.CharField(max_length=100, null=True, blank=True)
    Skin_desc = models.CharField(max_length=100, null=True, blank=True)
    Skin_image = models.ImageField(upload_to="Skin Images", null=True, blank=True)

class Nailservicedb(models.Model):
    Nailcat_name = models.CharField(max_length=100, null=True, blank=True)
    Nail_category = models.CharField(max_length=100, null=True, blank=True)
    Nail_name = models.CharField(max_length=100, null=True, blank=True)
    Nail_price = models.CharField(max_length=100, null=True, blank=True)
    Nail_desc = models.CharField(max_length=100, null=True, blank=True)
    Nail_image = models.ImageField(upload_to="Nail Images", null=True, blank=True)

class Makeupservicedb(models.Model):
    Makeupcat_name = models.CharField(max_length=100, null=True, blank=True)
    Makeup_category = models.CharField(max_length=100, null=True, blank=True)
    Makeup_name = models.CharField(max_length=100, null=True, blank=True)
    Makeup_price = models.CharField(max_length=100, null=True, blank=True)
    Makeup_desc = models.CharField(max_length=100, null=True, blank=True)
    Makeup_image = models.ImageField(upload_to="Makeup Images", null=True, blank=True)

class Bodycareservicedb(models.Model):
    Bodycarecat_name = models.CharField(max_length=100, null=True, blank=True)
    Bodycare_category = models.CharField(max_length=100, null=True, blank=True)
    Bodycare_name = models.CharField(max_length=100, null=True, blank=True)
    Bodycare_price = models.CharField(max_length=100, null=True, blank=True)
    Bodycare_desc = models.CharField(max_length=100, null=True, blank=True)
    Bodycare_image = models.ImageField(upload_to="BodyCare Images", null=True, blank=True)

class mycart(models.Model):
    cart_username=models.CharField(max_length=100, null=True, blank=True)
    cart_productname=models.CharField(max_length=100, null=True, blank=True)
    cart_qty=models.IntegerField(null=True, blank=True)
    cart_totalprice=models.IntegerField(null=True, blank=True)
