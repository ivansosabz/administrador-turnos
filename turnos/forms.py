from django import forms

from usuarios.models import Grupo
from .models import Responsable

class ResponsableForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['grupoFamiliar'].queryset = Grupo.objects.filter(usuario=user)

    class Meta:
        model = Responsable
        fields = [
            'nombre',
            'apellido',
            'color',
            'activo'
            'grupoFamiliar',
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={
                'type': 'color',
                'class': 'form-control'
            }),
            'grupoFamiliar': forms.Select(attrs={'class': 'form-select'}),
        }