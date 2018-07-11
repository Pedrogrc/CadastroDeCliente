from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lista', views.lista_clientes, name='lista_clientes'),
    path('novo', views.cadastro_cliente, name='cadastro_cliente'),
    path('atualizar/<int:pk>/', views.editar_cliente, name='editar_cliente'),
    path('delete/<int:pk>/', views.delete_cliente, name='delete_cliente'),
]