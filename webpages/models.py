from django.db import models

# Create your models here.



class HeroSection(models.Model):
    title= models.CharField(max_length=50)
    subtitle = models.CharField(max_length=150)
    buttontext = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='hero/')
    created_date = models.DateTimeField(auto_now_add=True)





class AboutSection(models.Model):
    title= models.CharField(max_length=50)
    subtitle = models.CharField(max_length=500)
    photo = models.ImageField(upload_to='about/')
    created_date = models.DateTimeField(auto_now_add=True)



class Service(models.Model):
    photo = models.ImageField(upload_to='services/')
    title= models.CharField(max_length=50)
    subtitle = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)


class Advantage(models.Model):
    photo = models.ImageField(upload_to='advantages/')
    title= models.CharField(max_length=50)
    subtitle = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)



class Work(models.Model):
    photo = models.ImageField(upload_to='works/')


class Testimonial(models.Model):
    personphoto = models.ImageField(upload_to='testimonials/')
    personname =  models.CharField(max_length=50)
    personjobpost =  models.CharField(max_length=50)
    testimonialstext= models.CharField(max_length=300)