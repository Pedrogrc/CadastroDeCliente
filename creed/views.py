from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Cliente
from .forms import ClienteForm


def index(request):
    return render(request,"index.html")


def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, "lista_clientes.html", {'clientes': clientes})


def editar_cliente(request, pk):
    cliente = Cliente.objects.get(pk=pk)
    form = ClienteForm(request.POST or None, instance=cliente)

    if form.is_valid():
        form.save()
        return redirect('lista_clientes')

    return render(request, 'atualizar_cliente.html', {'form': form})


def cadastro_cliente(request):

    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_clientes')

    return render(request, 'cadastro_cliente.html', {'form': form})


def delete_cliente(request, pk):
    clientes = Cliente.objects.get(pk=pk)
    clientes.delete()
    return redirect('lista_clientes')

# Create your views here.
