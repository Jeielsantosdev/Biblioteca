from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import CadastroUser


# Create your views here.


def cadastro_user(request):

    user = CadastroUser.objects.all()
    
    
    
    return render(request, 'create_user.html')