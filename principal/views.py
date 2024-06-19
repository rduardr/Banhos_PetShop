from django.shortcuts import render

from django.shortcuts import render
from principal.forms import ContatoForm


def inicio(request):
    return render(request, "inicio.html")


def contato(request):
    sucesso = False
    form = ContatoForm(request.POST or None)
    if form.is_valid():
        sucesso = True
        form.save()
    contexto = {
        "telefone": "(55) 9999-9999",
        "responsavel": "Sra. Lambeijos",
        "form": form,
        "sucesso": sucesso,
    }
    return render(request, "contato.html", contexto)

