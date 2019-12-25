from django.db import models

# Create your models here.
class Person(models.Model):
    primeiro_nome = models.CharField( max_length=50)
    ultimo_nome = models.CharField( max_length=50)
    idade = models.IntegerField()
    salario = models.DecimalField(max_digits=5, decimal_places=2)
    bio = models.TextField()
    foto = models.ImageField(upload_to='clients_photos', null=True, blank=True) #opcional

    def __str__(self):
        return self.primeiro_nome + ' ' + self.ultimo_nome
    