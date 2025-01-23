from django.db import models

# Create your models here.
class CadastroUser(models.Model):
    nome = models.CharField(max_length=33)
    email = models.EmailField()
    senha = models.CharField(max_length=64)
    data_nascimento = models.DateField()
    ativo = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.email