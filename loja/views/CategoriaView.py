from django.shortcuts import render, redirect
from loja.models import Categoria
from django.utils import timezone

def list_categoria_view(request, id=None):
    categorias = Categoria.objects.all()
    context = {
        'categorias': categorias
    }
    return render(request, template_name='categoria/categoria.html', context=context, status=200)

def edit_categoria_view(request, id=None):
    categorias = Categoria.objects.all()
    if id is not None:
        categorias = categorias.filter(id=id)
    categoria = categorias.first()
    print(categoria)
    context = { 'categoria': categoria }
    return render(request, template_name='categoria/categoria-edit.html', context=context, status=200)

def edit_categoria_postback(request, id=None):
    if request.method == 'POST':
        # Salva dados editados
        id = request.POST.get("id")
        categoria_nome = request.POST.get("Categoria")
        print("postback")
        print(id)
        print(categoria_nome)
        try:
            obj_categoria = Categoria.objects.filter(id=id).first()
            obj_categoria.Categoria = categoria_nome
            obj_categoria.save()
            print("Categoria %s salva com sucesso" % categoria_nome)
        except Exception as e:
            print("Erro salvando edição de categoria: %s" % e)
    return redirect("/categoria")

def details_categoria_view(request, id=None):
    categorias = Categoria.objects.all()
    if id is not None:
        categorias = categorias.filter(id=id)
    categoria = categorias.first()
    print(categoria)
    context = {'categoria' : categoria }
    return render(request, template_name='categoria/categoria-details.html', context=context, status=200)

def delete_categoria_view(request, id=None):
    # Processa o evento GET gerado pela action
    categorias = Categoria.objects.all()
    print(f"id (delete_categoria_view 1): {id}")
    if id is not None:
        categorias = categorias.filter(id=id)
    categoria = categorias.first()
    print(f"Categoria: {categoria}")
    print(f"id (delete_categoria_view 2): {id}")
    context = {'categoria' : categoria }
    return render(request, template_name='categoria/categoria-delete.html', context=context, status=200)

def delete_categoria_postback(request, id=None):
    if request.method == 'POST':
        id = request.POST.get("id")
        print(f"id (delete_categoria_postback): {id}")
        categoria_nome = request.POST.get("Categoria")
        print("postback-delete")
        print(id)
        try:
            Categoria.objects.filter(id=id).delete()
            print("Categoria %s excluida com sucesso" % categoria_nome)
        except Exception as e:
            print("Erro salvando edição de categoria: %s" % e)
    return redirect("/categoria")
        
def create_categoria_view(request, id=None):
    if request.method == 'POST':
        categoria_nome = request.POST.get("Categoria")
        print("postback-create")
        print(categoria_nome)
        try:
            obj_categoria = Categoria()
            obj_categoria.Categoria = categoria_nome
            obj_categoria.criado_em = timezone.now()
            obj_categoria.alterado_em = obj_categoria.criado_em
            obj_categoria.save()
            print("Categoria %s salva com sucesso" % categoria_nome)
        except Exception as e:
            print("Erro inserindo categoria: %s" % e)
        return redirect("/categoria")
    context = { 'categoria': None }
    return render(request, template_name='categoria/categoria-create.html', context=context, status=200)
