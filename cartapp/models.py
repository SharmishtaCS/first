from django.db import models

# Create your models here.

class Categorydb(models.Model):
    Cat_Name = models.CharField(max_length=30, null=True, blank=True)
    Mobile = models.IntegerField(null=True, blank=True)
