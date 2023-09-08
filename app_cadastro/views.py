from django.shortcuts import render
from .models import Usuarios

def home(request):
    return render(request, 'users/home.html')

def listagem(request):
    users = {
        'users': Usuarios.objects.all()
    }

    return render(request, 'users/users.html', users)

def listagem_users(request):
    new_user = Usuarios()
    new_user.nome = request.POST.get('nome')
    new_user.idade = request.POST.get('idade')
    new_user.save()

    users = {
        'users': Usuarios.objects.all()
    }

    return render(request, 'users/users.html', users)

