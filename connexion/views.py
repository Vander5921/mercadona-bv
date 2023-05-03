from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth import logout

def login_view(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if form.is_valid():
        login(request, form.get_user())
        return redirect('ajouter_article')

    return render(request, 'connexion/login.html', {'form': form})

def deconnexion(request):
    logout(request)
    return redirect('home')