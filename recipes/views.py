from django.shortcuts import render


def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Victor Abreu',
    })


def sobre(request):
    return render(request, 'recipes/sobre.html')


def contato(request):
    return render(request, 'recipes/contato.html')
