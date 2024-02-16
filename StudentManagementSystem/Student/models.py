from django.db import models
from Advisor.models import Advisor

# Create your models here.



class Student(models.Model):
    name = models.CharField(max_length = 150)
    department = models.CharField(max_length = 150)
    id_number = models.CharField(max_length = 150)
    year = models.CharField(max_length = 150)
    advisor = models.ForeignKey(Advisor, on_delete = models.CASCADE)

