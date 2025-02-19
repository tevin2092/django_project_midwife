from django.db import models
from django.contrib.auth.models import AbstractUser


class Midwife(AbstractUser):
    midwife_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"