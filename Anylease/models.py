from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

ITEM_CHOICES = [
    ('Electrical Equipments', 'Electrical Equipments'),
    ('Music Equipments', 'Music Equipments'),
    ('Electronic Equipments', 'Electronic Equipments'),
    ('Sports Equipments', 'Sports Equipments'),
    ('Building/Construction Equipments', 'Building/Construction Equipments'),
    ('IT Equipments', 'IT Equipments'),
    ('Audio/Visual Equipments', 'Audio/Visual Equipments'),
    ('Event Equipments', 'Event Equipments')
]


class Items(models.Model):
    Item_Category = models.CharField(max_length=32, choices=ITEM_CHOICES, default='green', null=False)
    Item_Amount = models.IntegerField(null=False)
    Item_Name = models.CharField(max_length=30)
    Image = models.ImageField(null=False, upload_to='images/')

    def __str__(self):
        return self.Item_Name


class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    last_login = models.DateTimeField


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.CharField(max_length=20)
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.phone_number


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.CharField(max_length=20)
    designation = models.CharField(max_length=50)

    def __str__(self):
        return self.phone_number
