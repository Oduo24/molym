from django.db import models

# Create your models here.
class GuestUser(models.Model):
    first_name = models.CharField(max_length=200)
    email_address = models.CharField(max_length=200)
    message = models.TextField()