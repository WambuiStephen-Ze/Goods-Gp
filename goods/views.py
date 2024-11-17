from django.shortcuts import render
from .models import Team
#
# def index(request):
#     teams = Team.objects.all()
#     context = {
#         'teams': teams
#
#
#
#     }
#     return render(request, 'index.html', context)
def index(request):
    return render(request, 'index.html')
# Create your views here.
def portfolio(request):
    return render(request, 'portfolio-details.html')

def services(request):
    return render(request, 'service-details.html')

def starter(request):
    return render(request, 'service-details.html')
def layout(request):
    return render(request, 'layout.html')