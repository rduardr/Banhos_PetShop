from django.utils import timezone
from django import forms
from reserva.models import Reserva, Petshop


class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = [
            "nome",
            "email",
            "nome_pet",
            "data",
            "turno",
            "tamanho",
            "petshop",
            "observacoes",
            
        ]

    petshop = forms.ModelChoiceField(queryset=Petshop.objects.all(), empty_label="Selecione um Petshop")

    def clean_data(self):
        data = self.cleaned_data.get("data")

        if data and data < timezone.now().date():
            raise forms.ValidationError("Não é possível agendar banhos para o passado.")

        if Reserva.objects.filter(data=data).count() >= 4:
            raise forms.ValidationError("Limite de reservas para este dia atingido.")

        return data
