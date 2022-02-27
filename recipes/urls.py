
from django.urls import path

from .views import contato, home, sobre

# dominio/recipes/
urlpatterns = [
    path('', home),
    path('sobre/', sobre),
    path('contato/', contato),
]
