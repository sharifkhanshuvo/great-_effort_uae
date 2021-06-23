from django.shortcuts import render
from .models import HeroSlider,Team,Service

# Create your views here.

def home(request):

    HeroSliders = HeroSlider.objects.all()
    AdministratorTeams=Team.objects.all().filter(teamtype='administrator')
    EngineeringTeams=Team.objects.all().filter(teamtype='engineering')
    MEPService=Service.objects.all().filter(category='mep')
    ContractingService=Service.objects.all().filter(category='contracting')

    data = {
        'herosliders':HeroSliders,
        'EngineeringTeams':EngineeringTeams,
        'AdministratorTeams':AdministratorTeams,
        'MEPService':MEPService,
        'ContractingService':ContractingService
    }
   


    return render(request,'webpages/home.html',data )




def about(request):
    return render(request, 'webpages/about.html')



def services(request):
    MEPService=Service.objects.all().filter(category='mep')
    ContractingService=Service.objects.all().filter(category='contracting')


    data  ={
        'MEPService':MEPService,
        'ContractingService':ContractingService
    }

    return render(request, 'webpages/service.html',data)

def portfolio(request):
    return render(request, 'webpages/portfolio.html')


def team(request):
    return render(request, 'webpages/team.html')

def contact(request):
    return render(request, 'webpages/contact.html')