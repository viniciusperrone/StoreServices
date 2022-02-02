from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4

# Create your models here.

def imageUpload(instance, filename):
    return f"{instance.id}-{filename}"

class Products(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=250)
    description = models.TextField(max_length=1000)
    price = models.FloatField()
    selling = models.BooleanField(default=False)
    image = models.ImageField(
        upload_to=imageUpload, 
        blank=True, 
        null=True
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)