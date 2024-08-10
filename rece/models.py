from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Reciepe(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    reciepe_image = models.ImageField(blank=True)

    def __str__(self) -> str:
        return self.name