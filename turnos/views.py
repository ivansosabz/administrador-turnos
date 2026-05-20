from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from turnos.forms import ResponsableForm, CicloForm
from turnos.models import Responsable, Ciclo


# Create your views here.
@login_required
def responsables(request):
    responsables = Responsable.objects.filter(grupo__usuario=request.user)
    return render(
        request,
        'responsables/responsables.html',
        {'responsables': responsables}
    )

@login_required
def responsables_crear(request):
    if request.method == 'POST':
        form = ResponsableForm(request.POST, user=request.user)
        if form.is_valid():
            # responsable = form.save(commit=False)
            # responsable.usuario = request.user
            form.save()
            return redirect('responsables')
    else:
        form = ResponsableForm(user=request.user)
    return render(
        request,
        'responsables/crear.html',
        {'form': form}
    )

@login_required
def responsables_editar(request, pk):
    responsable = get_object_or_404(Responsable, pk=pk)
    if responsable.grupo.usuario != request.user:
        return redirect('responsables')
    if request.method == 'POST':
        # form = ResponsableForm(request.POST, instance=responsable)
        form = ResponsableForm(request.POST, instance=responsable, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('responsables')
    else:
        # form = ResponsableForm(instance=responsable)
        form = ResponsableForm(instance=responsable, user=request.user)

    return render(
        request,
        'responsables/editar.html',
        {
            'form': form,
            'responsable': responsable
        }
    )

@login_required
def responsables_eliminar(request, pk):
    responsable = get_object_or_404(Responsable, pk=pk)
    if responsable.grupo.usuario != request.user:
        return redirect('responsables')
    if request.method == 'POST':
        responsable.delete()
        return redirect('responsables')
    return render(
        request,
        'responsables/eliminar.html',
        {'responsable': responsable}
    )

##---Ciclos---##
@login_required
def ciclos(request):
    ciclos = Ciclo.objects.filter(grupo__usuario=request.user) #Dame los ciclos cuyo grupo tenga como usuario al usuario logueado
    return render(
        request,
        'ciclos/ciclos.html',
        {'ciclos': ciclos}
    )
@login_required
def ciclos_crear(request):
    if request.method == 'POST':
        form = CicloForm(request.POST, user=request.user)
        if form.is_valid():
            ciclo = form.save()
            return redirect('ciclos_orden', ciclo_pk=ciclo.pk)
    else:
        form = CicloForm(user=request.user)
    return render(
        request,
        'ciclos/crear.html',
        {'form': form}
    )
@login_required
def ciclos_editar(request, pk):
    ciclo = get_object_or_404(Ciclo, pk=pk)
    if ciclo.grupo.usuario != request.user:
        return redirect('ciclos')
    if request.method == 'POST':
        form = CicloForm(request.POST, instance=ciclo, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('ciclos')
    else:
        form = CicloForm(user=request.user, instance=ciclo)
    return render(
        request,
        'ciclos/editar.html',
        {
            'form': form,
            'ciclo': ciclo
        }
    )
##---Ciclos Orden---##
@login_required
def ciclos_orden(request, ciclo_pk):
    ciclo = get_object_or_404(Ciclo, pk=ciclo_pk)
    return render(
        request,
        'ciclos_orden/ciclos_orden.html',
        {'ciclo': ciclo}
    )