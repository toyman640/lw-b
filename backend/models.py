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