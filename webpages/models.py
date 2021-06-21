from django.db import models

# Create your models here.

class HeroSlider(models.Model):
    title=models.CharField(max_length=50)
    subtitle=models.CharField(max_length=50)
    photo = models.ImageField(upload_to='heroSlider/')

    def __str__(self):
        return self.title


class About(models.Model):
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=300)
    photo= models.ImageField(upload_to='aboutus/')

    def __str__(self):
        return self.title


class Team(models.Model):
    TEAM_CHOICES= (
    (
        'administrator','administrator'
    ),
     (
        'engineering','engineering'
    ),
    )
    name=models.CharField(max_length=50)
    post=models.CharField(max_length=50)
    photo=models.ImageField(upload_to='teamimages/')
    teamtype=models.CharField(max_length=50,choices=TEAM_CHOICES)

    def __str__(self):
        return self.name


class Project(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=300)
    photo = models.ImageField(upload_to='projects/')
    def __str__(self):
        return self.name



class Service(models.Model):
    CATEGORY_CHOICES= (
    (
        'mep','mep'
    ),
     (
        'contracting','contracting'
    ),
    )
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=100)
    photo=models.ImageField(upload_to='services/')
    category=models.CharField(max_length=50,choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    personname=models.CharField(max_length=50)
    personprofession=models.CharField(max_length=50)
    testimonial=models.CharField(max_length=50)
    photo=models.ImageField(upload_to='testimonial/')

    def __str__(self):
        return self.personname