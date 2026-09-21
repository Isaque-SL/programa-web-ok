from django.shortcuts import render, redirect
from loja.models import Fabricante
from django.utils import timezone

def list_fabricante_view(request, id=None):
    fabricantes = Fabricante.objects.all()
    context = {
        'fabricantes': fabricantes
    }
    return render(request, template_name='fabricante/fabricante.html', context=context, status=200)

def edit_fabricante_view(request, id=None):
    fabricantes = Fabricante.objects.all()
    if id is not None:
        fabricantes = fabricantes.filter(id=id)
    fabricante = fabricantes.first()
    print(fabricante)
    context = { 'fabricante': fabricante }
    return render(request, template_name='fabricante/fabricante-edit.html', context=context, status=200)

def edit_fabricante_postback(request, id=None):
    if request.method == 'POST':
        # Salva dados editados
        id = request.POST.get("id")
        fabricante_nome = request.POST.get("Fabricante")
        print("postback")
        print(id)
        print(fabricante_nome)
        try:
            obj_fabricante = Fabricante.objects.filter(id=id).first()
            obj_fabricante.Fabricante = fabricante_nome
            obj_fabricante.save()
            print("Fabricante %s salvo com sucesso" % fabricante_nome)
        except Exception as e:
            print("Erro salvando edição de fabricante: %s" % e)
    return redirect("/fabricante")

def details_fabricante_view(request, id=None):
    fabricantes = Fabricante.objects.all()
    if id is not None:
        fabricantes = fabricantes.filter(id=id)
    fabricante = fabricantes.first()
    print(fabricante)
    context = {'fabricante' : fabricante }
    return render(request, template_name='fabricante/fabricante-details.html', context=context, status=200)

def delete_fabricante_view(request, id=None):
    # Processa o evento GET gerado pela action
    fabricantes = Fabricante.objects.all()
    print(f"id (delete_fabricante_view 1): {id}")
    if id is not None:
        fabricantes = fabricantes.filter(id=id)
    fabricante = fabricantes.first()
    print(f"Fabricante: {fabricante}")
    print(f"id (delete_fabricante_view 2): {id}")
    context = {'fabricante' : fabricante }
    return render(request, template_name='fabricante/fabricante-delete.html', context=context, status=200)

def delete_fabricante_postback(request, id=None):
    if request.method == 'POST':
        id = request.POST.get("id")
        print(f"id (delete_fabricante_postback): {id}")
        fabricante_nome = request.POST.get("Fabricante")
        print("postback-delete")
        print(id)
        try:
            Fabricante.objects.filter(id=id).delete()
            print("Fabricante %s excluido com sucesso" % fabricante_nome)
        except Exception as e:
            print("Erro salvando edição de fabricante: %s" % e)
    return redirect("/fabricante")
        
def create_fabricante_view(request, id=None):
    if request.method == 'POST':
        fabricante_nome = request.POST.get("Fabricante")
        print("postback-create")
        print(fabricante_nome)
        try:
            obj_fabricante = Fabricante()
            obj_fabricante.Fabricante = fabricante_nome
            obj_fabricante.criado_em = timezone.now()
            obj_fabricante.alterado_em = obj_fabricante.criado_em
            obj_fabricante.save()
            print("Fabricante %s salvo com sucesso" % fabricante_nome)
        except Exception as e:
            print("Erro inserindo fabricante: %s" % e)
        return redirect("/fabricante")
    context = { 'fabricante': None }
    return render(request, template_name='fabricante/fabricante-create.html', context=context, status=200)
