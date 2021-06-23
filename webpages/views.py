from django.shortcuts import render
from .models import HeroSlider,Team,Service,About,Client,Project

# Create your views here.

def home(request):

    HeroSliders = HeroSlider.objects.all()
    AdministratorTeams=Team.objects.all().filter(teamtype='administrator')
    EngineeringTeams=Team.objects.all().filter(teamtype='engineering')
    MEPService=Service.objects.all().filter(category='mep')
    ContractingService=Service.objects.all().filter(category='contracting')
    aboutVar=About.objects.all()
    clients=Client.objects.all()

    data = {
        'herosliders':HeroSliders,
        'EngineeringTeams':EngineeringTeams,
        'AdministratorTeams':AdministratorTeams,
        'MEPService':MEPService,
        'ContractingService':ContractingService,
        'aboutVar':aboutVar,
        'clients':clients

        
    }
   



    return render(request,'webpages/home.html',data )




def about(request):
    aboutVar=About.objects.all()
    data = {
        
        'aboutVar':aboutVar,
        

        
    }
    return render(request, 'webpages/about.html',data)



def services(request):
    MEPService=Service.objects.all().filter(category='mep')
    ContractingService=Service.objects.all().filter(category='contracting')


    data  ={
        'MEPService':MEPService,
        'ContractingService':ContractingService
    }

    return render(request, 'webpages/service.html',data)

def portfolio(request):
    projects=Project.objects.all()
    data={
        'projects':projects
    }
    return render(request, 'webpages/portfolio.html',data)


def team(request):
    AdministratorTeams=Team.objects.all().filter(teamtype='administrator')
    EngineeringTeams=Team.objects.all().filter(teamtype='engineering')
    data = {
     
        'EngineeringTeams':EngineeringTeams,
        'AdministratorTeams':AdministratorTeams,
       
        
    }
    return render(request, 'webpages/team.html',data)

def contact(request):
    return render(request, 'webpages/contact.html')



def blogs(request):
    return render(request, 'webpages/blogs.html')