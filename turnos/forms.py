from django import forms

from usuarios.models import Grupo
from .models import Responsable, Ciclo, CicloOrden

class ResponsableForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['grupo'].queryset = Grupo.objects.filter(usuario=user)

    class Meta:
        model = Responsable
        fields = [
            'nombre',
            'apellido',
            'color',
            'activo',
            'grupo',
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={
                'type': 'color',
                'class': 'form-control'
            }),
            'grupo': forms.Select(attrs={'class': 'form-select'}),
        }

class CicloForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['grupo'].queryset = Grupo.objects.filter(usuario=user)
    class Meta:
        model = Ciclo
        fields = [
            'intervalo_dias',
            'fecha_inicio',
            'activo',
            'grupo',
        ]
        widgets = {
        'intervalo_dias': forms.NumberInput(attrs={'class': 'form-control'}),
        'fecha_inicio': forms.DateInput(attrs={'class': 'form-control'}),
        'activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'grupo': forms.Select(attrs={'class': 'form-select'}),
        }

class CicloOrdenForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['responsable'].queryset = Responsable.objects.filter(grupo__usuario=user)

    class Meta:
        model = CicloOrden
        fields = [
            'posicion',
            'responsable'
        ]
        widgets = {
            'posicion': forms.NumberInput(attrs={'class': 'form-select'}),
            'responsable': forms.Select(attrs={'class': 'form-select'}),
        }