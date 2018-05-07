from django.shortcuts import render, redirect
from .models import Produto
from .forms import ProductForm
# Create your views here.
def listar_todos_produtos(request):
    produtos = Produto.objects.all()
    #Produto.objects.get(id=1)
    return render(request, 'produtos.html',{'produtos':produtos})

def criar_novo_produto(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_todos_produtos')
    return render(request, 'products-form.html',{'form':form})

def update_produto(request, id):
    produto = Produto.objects.get(id=id)
    form = ProductForm(request.POST or None, instance=produto)
    if form.is_valid():
        form.save()
        return redirect('listar_todos_produtos')
    return render(request, 'products-form.html',{'form':form})

def delete_produto(request, id):
    produto = Produto.objects.get(id=id)
    if request.method == 'GET':
        produto.delete()
        return redirect('listar_todos_produtos')
