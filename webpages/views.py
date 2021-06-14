from django.shortcuts import render

from .models import HeroSection, AboutSection, Service, Advantage, Work, Testimonial
# Create your views here.

def home(request):
    Hero = HeroSection.objects.all()
    About = AboutSection.objects.all()
    Services = Service.objects.all()
    Advantages = Advantage.objects.all()
    Works = Work.objects.all()
    Testimonials = Testimonial.objects.all()



    data ={
        'hero':Hero[0],
        'about':About[0],
        'services':Services,
        'advantages':Advantages,
        'works':Works,
        'testimonials':Testimonials
    }


    return render(request,'webpages/home.html',data )




def about(request):
    return render(request, 'webpages/about.html')



def services(request):

    return render(request, 'webpages/services.html'  )


def projects(request):
    return render(request, 'webpages/projects.html')



def team(request):
    return render(request, 'webpages/team.html')