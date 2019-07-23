from django.shortcuts import render
from .models import Rezept


def home(request):
    context = {
        'rezepte': Rezept.objects.all()
    }
    return render(request, 'wmarkt/home.html', context)


def about(request):
    return render(request, 'wmarkt/about.html', {'title': 'Über Wochenmarkt'})


def register(request):
    return render(request, 'wmarkt/register.html', {'title': 'Willkommen beim Wochenmarkt'})
