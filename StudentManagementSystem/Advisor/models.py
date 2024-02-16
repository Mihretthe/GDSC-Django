from django.db import models

# Create your models here.

class Advisor(models.Model):    
    name = models.CharField(max_length = 150)
    lname = models.CharField(max_length = 150)
    department = models.CharField(max_length = 150)
    
