from django.shortcuts import render


# Create your views here.

def home(request):
   


    return render(request,'webpages/home.html' )




def about(request):
    return render(request, 'webpages/about.html')



def services(request):
    return render(request, 'webpages/service.html')

def portfolio(request):
    return render(request, 'webpages/portfolio.html')


def team(request):
    return render(request, 'webpages/team.html')

def contact(request):
    return render(request, 'webpages/contact.html')