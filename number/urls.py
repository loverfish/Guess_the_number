from django.urls import path

from .views import *


urlpatterns = [
    path('', start_game, name='start_game'),
    path('go', guess, name='guess'),
]
