from django.db import models

# Create your models here.

class delete_user(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=100)

    class Meta:
        db_table ="users"