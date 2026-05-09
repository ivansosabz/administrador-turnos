from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserForm, GrupoForm
from django.contrib.auth.decorators import login_required

from .models import Grupo


# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserForm()
    return render(
        request,
        'usuarios/signup.html',
        {'form': form}
    )
@login_required
def grupo(request):
    grupos = Grupo.objects.filter(usuario = request.user)
    return render(
        request,
        'grupos/grupos.html',
        {'grupos': grupos}
    )
@login_required
def crear_grupo(request):
    if request.method == 'POST':
        form = GrupoForm(request.POST)
        if form.is_valid():
            grupo = form.save(commit=False) #sirve para que cree en objeto pero que aun no lo guarde en la bd, porque si guardas usuario dara error
            grupo.usuario = request.user #el usuario logueado en ese momento
            grupo.save()
            return redirect('grupo')
    else:
        form = GrupoForm()
    return render(
        request,
        'grupos/crear.html'
        ,{'form': form}
    )
@login_required
def editar_grupo(request, pk):
    grupo = get_object_or_404(Grupo, pk=pk) #seleccionando grupo
    if grupo.usuario != request.user:
        return redirect('grupo')
    if request.method == 'POST':
        form = GrupoForm(request.POST, instance=grupo) #instace=grupo para que muestre los datos cuales
        if form.is_valid():
            form.save()
            return redirect('grupo')
    else:
        #si es get solo muestra el formulario con los datos
        form = GrupoForm(instance=grupo)
    return render(
        request,
        'grupos/editar.html',
        {
            'grupo': grupo,
            'form': form
        }
    )
