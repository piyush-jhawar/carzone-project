from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator, MaxValueValidator

from datetime import date
from phonenumbers import PhoneNumber

# Create your models here.


class Team(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    email = models.EmailField(max_length=254, unique=True)
    mobile = PhoneNumberField(unique=True)
    emergency_contact = PhoneNumberField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    facebook_link = models.URLField(max_length=200, unique=True, blank=True)
    twitter_link = models.URLField(max_length=200, unique=True, blank=True)
    instagram_link = models.URLField(max_length=200, unique=True, blank=True)
    linkedIn_link = models.URLField(max_length=200, unique=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class CompanyDetail(models.Model):
    title = models.CharField(max_length=255)
    mobile = PhoneNumberField(unique=True)
    fax = PhoneNumberField(unique=True, null=True, blank=True)
    email = models.EmailField(max_length=254, unique=True)
    web = models.URLField(max_length=200, unique=True)
    startday = models.CharField(max_length=20)
    endday = models.CharField(max_length=20)
    opentime = models.CharField(max_length=10)
    closetime = models.CharField(max_length=10)
    # copyright_year = models.DecimalField(max_digits=4, decimal_places=0, default=date.today().year, validators=[MinValueValidator(date.today().year-2), MaxValueValidator(date.today().year)])
    facebook = models.URLField(max_length=200, unique=True, blank=True)
    twitter = models.URLField(max_length=200, unique=True, blank=True)
    instagram = models.URLField(max_length=200, unique=True, blank=True)
    linkedIn = models.URLField(max_length=200, unique=True, blank=True)
    rss = models.URLField(max_length=200, unique=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"





# photo
# firstname
# lastname
# email
# mobile
# designation
# facebooklink
# twitterlink
# googlepluslink
# createddate
# modifieddate
