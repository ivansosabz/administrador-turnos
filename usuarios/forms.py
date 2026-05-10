from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Grupo

class UserForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Tu email'
        })
    )

    #opcional: personalizar widgets, tarea para después
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Tu contraseña'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirma tu contraseña'})

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Tu nombre de usuario'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Tu email'
            }),
        }


class GrupoForm(forms.ModelForm):
    class Meta:
        model = Grupo
        # no ponemos usuarios en fields porque ya se asigna automaticamente
        fields = ('nombre',)
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }