from django.db import models

# Create your models here.
class image_db(models.Model):
    image_url = models.CharField(max_length=200)
    name = models.CharField(max_length=50)