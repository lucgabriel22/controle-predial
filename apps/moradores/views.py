from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import (
    render, 
    redirect, 
    get_object_or_404
    
)

from apps.moradores.forms import MoradorForm
from moradores.models import Moradores
from django.contrib.auth.decorators import login_required




@login_required
def registrar_morador(request):

    form = MoradorForm()

    if request.method == "POST":
        form = MoradorForm(request.POST)

        if form.is_valid():
            morador = form.save(commit=False)
            morador.registrado_por = request.user.porteiro

            morador.save()

            messages.success(
                request,
                "Morador registrado com sucesso"
            )

            return redirect("index")

    context = {
        "nome_pagina": "Registrar morador",
        "form": form,
    }

    return render(request, "registrar_morador.html", context)


@login_required
def view_morador(request):
    moradores = Moradores.objects.all()

    

    context = {
        "nome_pagina": "Lista de moradores",
        "moradores": moradores,
    }

    return render(request, "view_morador.html", context)

def info_morador(request, id):
    
    
    morador = get_object_or_404(Moradores, id=id)

    context = {
        "nome_pagina": "Informações do morador",
        "morador": morador,
    }

    return render(request, "info_morador.html", context)





