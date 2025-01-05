from django.contrib.admindocs.utils import ROLES
from django.contrib.auth.models import AbstractUser
from django.db import models


#Abstract User Model which handles authentication
class User(AbstractUser):
    USERNAME_FIELD = 'email'
    email = models.EmailField(unique=True)  # changes email to unique and blank to false
    REQUIRED_FIELDS = []  # removes email from REQUIRED_FIELDS
    class Role(models.TextChoices):
        ADMIN = 'ADMIN', 'Admin'
        USER = 'USER', 'User'

    base_role = Role.USER

    role = models.CharField(max_length=50, choices=Role.choices)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
        return super().save(*args, **kwargs)








