from django.db import models

from authentication.models import User


# Create your models here.

class Analyses(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    document_name = models.CharField(max_length=100)
    analyses = models.JSONField()


