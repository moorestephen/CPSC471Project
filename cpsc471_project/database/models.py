from django.db import models

# Create your models here.
class Admin(models.Model):
    email = models.EmailField(unique = True)
    tenure_start = models.DateField()
    fname = models.CharField(max_length = 15)
    lname = models.CharField(max_length = 30)
    club_name = models.CharField(max_length = 50)
