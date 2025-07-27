# from django.db import models

# # Create your models here.
# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField(blank=True)
#     price = models.FloatField()
#     def __str__(self):
#         return self.name

# class UserRegistration(models.Model):
#     full_name = models.CharField(max_length=100)
#     username = models.CharField(max_length=100,unique=True)
#     email = models.EmailField(unique=True)
#     phone = models.CharField(max_length=13)
#     password = models.CharField(max_length=100)
#     def __str__(self):
#         return self.username

from django.db import models

# Create your models here.
class Patient(models.Model):
    patient_id = models.BigAutoField(primary_key=True)
    first_name= models.CharField(max_length=50)
    last_name= models.CharField(max_length=50)
    blood= models.CharField(max_length=50)

    def __str__(self):
        return self.first_name