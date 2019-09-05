    
from django.db import models

class Register(models.Model):
    
    username=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=30)
    
    def __unicode__(self):
        return self.username

    def __str__(self):
        return self.username


class ProductData(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    role = models.CharField(max_length=50)
   
    