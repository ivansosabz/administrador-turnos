from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Grupo

class UserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    #opcional: personalizar widgets, tarea para después
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
    """


class GrupoForm(forms.ModelForm):
    class Meta:
        model = Grupo
        # no ponemos usuarios en fields porque ya se asigna automaticamente
        fields = ('nombre',)
        """
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }
        """