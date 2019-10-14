from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique = True, max_length=255)
    phone = models.CharField(null=True,max_length=255)
    REQUIRED_FIELDS = ['username','phone','first_name','last_name']
    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.email