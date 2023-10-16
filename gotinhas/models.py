from django.db import models

class Gotinhas(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthdate = models.DateField()
    number = models.IntegerField(default=0)
    # Adicione outros campos conforme necessário
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        # Verifica se é um novo "Gotinha" (id é None)
        if self.pk is None:
            # Encontra o número mais alto atualmente e incrementa em 1
            max_number = Gotinhas.objects.all().aggregate(models.Max('number'))['number__max']
            if max_number is not None:
                self.number = max_number + 1
            else:
                self.number = 1
        super(Gotinhas, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Obtém o número do "Gotinha" que está sendo excluído
        deleted_number = self.number
        super(Gotinhas, self).delete(*args, **kwargs)

        # Atualiza os números dos "Gotinhas" restantes
        Gotinhas.objects.filter(number__gt=deleted_number).update(number=models.F('number') - 1)