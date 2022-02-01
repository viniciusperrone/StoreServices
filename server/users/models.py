from distutils.command.upload import upload
from django.db import models
from uuid import uuid4
# Create your models here.

def avatarImage(instance, filename):
    return f"{instance.id}-{filename}"

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=250)
    password = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to=avatarImage, blank=True, null=True)
