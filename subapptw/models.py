from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Twitter(models.Model):
    name = models.CharField(
        'name', blank=False, default='Anonymous', max_length=20
    )
    body = models.CharField(
        blank=False, default='Anonymous', max_length=150
    )
    likes = models.IntegerField(
        blank=True, default=0
    )
    image = CloudinaryField(
        blank=True
    )
    created_at = models.DateTimeField(
        blank=True, auto_now_add=True
    )