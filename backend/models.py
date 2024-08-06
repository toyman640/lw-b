from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomerUser(AbstractUser):
  phone_number = models.CharField(max_length=15, blank=True, null=True)
  means_of_id = models.FileField(blank=True)
  avartar = models.ImageField(upload_to='avatars/', blank=True)
  countrty = models.CharField(max_length=10, blank=True, null=True)
  state = models.CharField(max_length=10, blank=True, null=True)


  def __str__(self):
    return self.username

class Category(models.Model):
  BUILDING = 'building'
  LAND = 'land'
  APARTMENT = 'apartment'

  CATEGORY_CHOICES = [
    (BUILDING, 'Building'),
    (LAND, 'Land'),
    (APARTMENT, 'Apartment'),
  ]

  name = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
  def __str__(self):
    return self.name

class PropertyImage(models.Model):
  image = models.ImageField(upload_to='property_images/')
  description = models.CharField(max_length=255, blank=True)

  def __str__(self):
    return self.description or "Property Image"

class Property(models.Model):
  title = models.CharField(max_length=255)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  images = models.ManyToManyField(PropertyImage, blank=True)  # No quotes needed
  country = models.CharField(max_length=100)
  state = models.CharField(max_length=100)
  area = models.CharField(max_length=100)
  category = models.CharField(max_length=100)
  description = models.TextField()
  posted_by = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
  approved = models.BooleanField(default=False)

  def __str__(self):
    return self.title