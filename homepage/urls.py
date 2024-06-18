from django.urls import path
from . import views
from homepage.views import cachorros

urlpatterns = [
    path('', views.CadastroView, name = 'home'),
    path('cachorros/',cachorros, name='cachorros')
]