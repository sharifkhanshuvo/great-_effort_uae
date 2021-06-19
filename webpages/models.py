from django.db import models

# Create your models here.

class HeroSlider(models.Model):
    title=models.CharField(max_length=50)
    subtitle=models.CharField(max_length=50)
    photo = models.ImageField(upload_to='heroSlider/')





