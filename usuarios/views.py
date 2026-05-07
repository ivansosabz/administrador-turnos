from django.shortcuts import render, redirect
from .forms import UserForm, GrupoForm

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
