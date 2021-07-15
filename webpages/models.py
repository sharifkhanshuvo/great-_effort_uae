from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime
# Create your models here.

class HeroSlider(models.Model):
    title=models.CharField(max_length=50)
    subtitle=models.CharField(max_length=50)
    photo = models.ImageField(upload_to='heroSlider/')

    def __str__(self):
        return self.title


class About(models.Model):
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=4000)
    photo= models.ImageField(upload_to='aboutus/')

    def __str__(self):
        return self.title

class ExpertWorker(models.Model):
    description=models.CharField(max_length=4000)
    def __str__(self):
        return 'Expert Worker Description'
class QualityWork(models.Model):
    description=models.CharField(max_length=4000)
    def __str__(self):
        return 'QualityWork Description'

class Support(models.Model):
    description=models.CharField(max_length=4000)
    def __str__(self):

        return 'Support Description'

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
    mobileno=models.CharField(max_length=50,default=971544568754)
    email=models.CharField(max_length=50,default='gegc2010@gmail.com')
    photo=models.ImageField(upload_to='teamimages/')
    teamtype=models.CharField(max_length=50,choices=TEAM_CHOICES)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    CATEGORY_CHOICES=(
        ('completed','completed'),
        ('running','running'),
        ('majorprojects','majorprojects'),

    )
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=300,default='description')
    photo = models.ImageField(upload_to='projects/')
    category=models.CharField(max_length=40,choices=CATEGORY_CHOICES,default='completed')
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



class Blog(models.Model):
    title=models.CharField(max_length=100)
    blogsubtitle=models.CharField(max_length=2000,default='blog subtitle')
    blogbody=RichTextField()
    blogthumbnail=models.ImageField(upload_to='blogthumbnail/')
    blogwriter=models.CharField(max_length=200,default=None)
    blogwriterinfo=models.CharField(max_length=500,default=None)
    blogwriterphoto=models.ImageField(upload_to='blogwriterphoto/',default=None)

    def __str__(self):
        return self.title



class Client(models.Model):
    companylogo=models.ImageField(upload_to='companylogo/')
    companyname=models.CharField(max_length=100)

    def __str__(self):
        return self.companyname



class AboutMore(models.Model):
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=4000)
    photo= models.ImageField(upload_to='aboutmore/')

    def __str__(self):
        return self.title


class ContactForm(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    mobileno=models.CharField(max_length=100,default=None)
    subject=models.CharField(max_length=1000)
    message=models.CharField(max_length=5000)


    def __str__(self):
        return self.name


class ExpertWorkerCount(models.Model):
    count=models.IntegerField()
    def __str__(self):
        return 'ExpertWorkerCount'
class ClientsCount(models.Model):
    count=models.IntegerField()
    def __str__(self):
        return 'ClientsCount'

class CompletedProjectCount(models.Model):
    count=models.IntegerField()
    def __str__(self):
        return 'CompletedProjectCount'

class RunningProjectCount(models.Model):
    count=models.IntegerField()
    def __str__(self):
        return 'ExpertWorkerCount'