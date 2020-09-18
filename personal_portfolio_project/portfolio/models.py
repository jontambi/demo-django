from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    image = models.ImageField(upload_to='portfolio/images/')
    ulr = models.URLField(blank=True)
