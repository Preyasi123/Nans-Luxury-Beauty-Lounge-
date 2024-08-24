from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contactdb(models.Model):
    contact_name = models.CharField(max_length=10, null=True, blank=True)
    contact_mail = models.EmailField(max_length=10, null=True, blank=True)
    contact_sub = models.CharField(max_length=10, null=True, blank=True)
    contact_msg = models.CharField(max_length=10, null=True, blank=True)


class signupdb(models.Model):
    signup_name=models.CharField(max_length=100, null=True, blank=True)
    signup_pwd=models.CharField(max_length=100, null=True, blank=True)
    signup_cpwd=models.CharField(max_length=100, null=True, blank=True)
    signup_mail=models.EmailField(max_length=100, null=True, blank=True)


class Appointmentdb(models.Model):
    app_user = models.CharField(max_length=100, null=True, blank=True)
    app_mail = models.EmailField(max_length=100, null=True, blank=True)
    app_mob = models.IntegerField(max_length=100, null=True, blank=True)
    app_place = models.IntegerField(max_length=100, null=True, blank=True)
    app_enquiry = models.TextField(max_length=100, null=True, blank=True)
    app_date = models.DateField(max_length=100, null=True, blank=True)
    app_time = models.TimeField()

class Bookdb(models.Model):
    book_user = models.CharField(max_length=100, null=True, blank=True)
    book_mail = models.EmailField(max_length=100, null=True, blank=True)
    book_mob = models.IntegerField(max_length=100, null=True, blank=True)
    book_service = models.CharField(max_length=100, null=True, blank=True)
    book_sername = models.CharField(max_length=100, null=True, blank=True)
    book_price = models.CharField(max_length=100, null=True, blank=True)
    book_date = models.DateField(max_length=100, null=True, blank=True)
    book_time = models.TimeField()


