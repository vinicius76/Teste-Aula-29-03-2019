from django.db import models
from django.contrib.auth.models import User

class Agenda(models.Model):
    data = models.DateField('Data do compromisso:',blank=True,null=True)

class Agenda_Institucional(Agenda):
    nome  = models.CharField("Nome do compromisso:",max_length=64,blank=True,null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

class Agenda_Publica(Agenda):
    nome = models.CharField('Nome do compromisso:',max_length=64,blank=True,null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    