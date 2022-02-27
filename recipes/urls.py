
from django.urls import path

from .views import home

# dominio/recipes/
urlpatterns = [
    path('', home),
]
