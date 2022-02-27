from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Victor Abreu',
    })


def sobre(request):
    return HttpResponse('Sobre')


def contato(request):
    return HttpResponse('Contato')
