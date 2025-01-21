from django.db import models # type: ignore
from .models import*
# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=30)
    address=models.CharField(max_length=50)
    phone=models.IntegerField()

    def _str_(self) -> str:
        return self.name