from django.urls import path
from.import views

app_name = 'appCorreios'

urlpatterns = [
    path('', views.home, name= 'home'),
    path('Cadastro/', views.cadastro, name= 'cadastro'),
    path('Lista/', views.lista, name= 'lista'),
    path('Cadastrar/', views.cadastrar, name= 'cadastrar'),

]