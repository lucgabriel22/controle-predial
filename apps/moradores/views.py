from django.contrib import messages
from django.shortcuts import (
    render, 
    redirect, 
    get_object_or_404
)
from .forms import MoradorForm
from .models import Moradores



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




