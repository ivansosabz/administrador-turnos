from django import forms
from .models import Responsable

class ResponsableForm(forms.ModelForm):
    class Meta:
        model = Responsable
        fields = [
            'nombre',
            'apellido',
            'color',
            'activo'
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={
                'type': 'color',
                'class': 'form-control'
            }),
        }