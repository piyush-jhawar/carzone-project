from datetime import datetime
from django.db import models
from cars.choice_car_model import state_choice, year_choice, door_choices, features_choices
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField

# Create your models here.


class Car(models.Model):
    car_title = models.CharField(max_length=255)
    state = models.CharField(choices=state_choice, max_length=100)
    city = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField(('year'), choices=year_choice, default=datetime.now().year)
    condition = models.CharField(max_length=100)
    price = models.IntegerField()
    # description = models.TextField(max_length=600)
    description = RichTextField()
    car_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    car_photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    car_photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    car_photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    car_photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    # features = models.CharField(choices=features_choices, max_length=255)
    features = MultiSelectField(choices=features_choices)
    body_style = models.CharField(max_length=100)
    engine = models.CharField(max_length=100)
    transmission = models.CharField(max_length=100)
    interior = models.CharField(max_length=100)
    miles = models.IntegerField()
    doors = models.CharField(choices=door_choices, max_length=5)
    passenger = models.IntegerField()
    VIN_no = models.CharField(max_length=100)
    mileage = models.IntegerField()
    fuel_type = models.CharField(max_length=15)
    no_of_owners = models.CharField(max_length=100)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    # created_date = models.DateTimeField(default=datetime.now, blank=True)
    modified_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.car_title}"


# car_title
# city
# state
# model
# year
# condition
# price
# description
# car_photo
# car_photo1
# car_photo2
# car_photo3
# car_photo4
# car_features
# body_style
# engine
# transmission
# interior
# miles
# doors
# passengers
# vin_no
# mileage
# fuel_type
# no_of_owners
# is_featured
# created_date
# modified_date
