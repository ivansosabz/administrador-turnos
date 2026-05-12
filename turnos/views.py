from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from turnos.forms import ResponsableForm
from turnos.models import Responsable

# Create your views here.
@login_required
def responsables(request):
    responsables = Responsable.objects.filter(grupoFamiliar__usuario=request.user)
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
    if responsable.grupoFamiliar.usuario != request.user:
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
    if responsable.grupoFamiliar.usuario != request.user:
        return redirect('responsables')
    if request.method == 'POST':
        responsable.delete()
        return redirect('responsables')
    return render(
        request,
        'responsables/eliminar.html',
        {'responsable': responsable}
    )