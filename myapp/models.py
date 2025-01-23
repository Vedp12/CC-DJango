from django.db import models # type: ignore
from .models import*
# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=200)
    description=models.CharField(max_length=200)
    
    def __str__(self):
        return self.name