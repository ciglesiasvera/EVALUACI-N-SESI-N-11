from django.shortcuts import render, redirect
from .forms import RegistroUsuarioForm
from django.contrib.auth import login

# Create your views here.

def crear_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('home')  
    else:
        form = RegistroUsuarioForm()
    return render(request, 'usuarios/crear_usuario.html', {'form': form})
