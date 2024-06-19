from django import forms
from principal.models import Contato


class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ["nome", "email", "assunto", "mensagem"]
