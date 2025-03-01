from django.db import models

from django.db import models

class Diretor(models.Model):
    nomeDiretor = models.CharField(max_length=255)
    idade = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nomeDiretor


class Filme (models.Model):
    tituloFilme = models.CharField(max_length=255)
    anoFilme = models.IntegerField()
    generoFilme = models.CharField(max_length=255)
    diretoFilme = models.ForeignKey(Diretor, on_delete=models.CASCADE, related_name='filmes')
    omdbId = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.tituloFilme