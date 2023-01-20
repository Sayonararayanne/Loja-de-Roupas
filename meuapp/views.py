from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Roupa
from .forms import RoupaForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'index.html')

@login_required
def crud_Roupas(request):
    roupas = Roupa.objects.all().order_by('tipo_de_roupa')
    conteudo = {"roupas": roupas}
    return render(request, 'roupas/crud.html', conteudo)    

@login_required
def criar_Roupas(request):
    formulario = RoupaForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect("crud_Roupas") 

    conteudo = {"formulario": formulario}
    return render(request, 'roupas/create.html', conteudo) 


def listar_Roupas(request):
    roupas = Roupa.objects.all().order_by('tipo_de_roupa')
    conteudo = {"roupas": roupas}

    return render(request, 'roupas/listagem.html', conteudo) 

@login_required
def editar_Roupas(request, pk):
    roupa = Roupa.objects.get(pk=pk)
    formulario = RoupaForm(request.POST or None, instance=roupa)
    if formulario.is_valid():
        formulario.save()
        return redirect("crud_Roupas") 

    conteudo = {"formulario": formulario, "roupa": roupa}
    return render(request, 'roupas/update.html', conteudo)

@login_required
def delete_Roupas(request, pk):
    roupa = Roupa.objects.get(pk=pk)
    roupa.delete()
    return redirect("crud_Roupas") 

def consulta(request):
    if request.method == 'GET':    
        pesquisa = request.GET.get('pesquisa')
        if pesquisa is None: 
            pesquisa = ''
        resultados = Roupa.objects.filter(tipo_de_roupa__icontains=pesquisa).order_by('tipo_de_roupa')
        print(resultados)
        return render(request, "consulta.html", { 'roupas': resultados, 'pesquisa': pesquisa })

def sobre(request):
    return render(request, 'sobre.html')