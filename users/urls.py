from django.urls import path
from . import views

urlpatterns = [
    path('cadastro-user/',views.cadastro_user, name='cadastro-user')
]
