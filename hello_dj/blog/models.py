from django.db import models


# Create your models here.

class BlogModel(models.Model):
    title = models.CharField(max_length=100, blank=True)
    content = models.TextField()

