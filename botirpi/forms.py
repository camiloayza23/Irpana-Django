from django import forms
from db.models import Zonas, Tipos

class IrpiForm(ModelForm):
    allTipos = forms.ModelChoiceField(queryset=Zonas.objects.all())
    allZonas = forms.ModelChoiceField(queryset=Tipos.objects.all())