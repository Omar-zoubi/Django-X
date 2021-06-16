from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.
class Snack(models.Model):
    title = models.CharField(max_length=100)
    purcheser = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    description = models.TextField(default=0)


    def get_absolute_url(self):
        return reverse("details", args=[str(self.id)])


def __str__(self):
    return self.name 