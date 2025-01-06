from django.db import models

from authentication.models import User


# Create your models here.

class Analysis(models.Model):
    user = models.ForeignKey(User, related_name="analysis", on_delete=models.CASCADE)
    document_name = models.CharField(max_length=100)
    analysis = models.JSONField()

    def __str__(self):
        return f"{self.user.email} - {self.document_name}"


