from django.db import models
from gotinhas.models import Gotinhas  # Certifique-se de importar corretamente o modelo do aplicativo 'usuarios'

class Atividade(models.Model):
    nome = models.CharField(max_length=255)
    foto = models.ImageField(upload_to='atividades_fotos/', null=True, blank=True)
    professor = models.CharField(max_length=255)
    alunos = models.ManyToManyField(Gotinhas, through='Presenca')

    def __str__(self):
        return self.nome
    
class Presenca(models.Model):
    atividade = models.ForeignKey(Atividade, on_delete=models.CASCADE)
    aluno = models.ForeignKey(Gotinhas, on_delete=models.CASCADE)
    data = models.DateField()
    turma = models.CharField(max_length=50)
    falta = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.aluno} - {self.atividade.nome} - {self.data}'