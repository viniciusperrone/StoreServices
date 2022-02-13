from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4
# Create your models here.

def avatarImage(instance, filename):
    return f"{instance.id}-{filename}"

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=250, unique=True)
    password = models.CharField(max_length=50)
    avatar = models.ImageField(
        upload_to=avatarImage, 
        blank=True, 
        null=True
    )
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []