from django.utils.translation import gettext_lazy as _
from django import forms
from .models import *

class RoupaForm(forms.ModelForm):
    class Meta:
        model = Roupa
        fields = ['tipo_de_roupa', 'cor', 'tamanho', 'preco', 'quantidade']
