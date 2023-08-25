from django.urls import path
from . import views

app_name = 'pedidos'

urlpatterns = [

]

# Adicione as URLs de cliente aqui
urlpatterns += [
    path('cliente/add/', views.ClienteCreateView.as_view(), name='cliente-add'),
]
