from django.db import models

# Create your models here.
class Esame (models.Model):
    id = models.AutoField(primary_key=True) 
    data_ora = models.DateField()
    tipo = models.CharField(max_length=255)
    esito = models.CharField(max_length=255)
    struttura = models.CharField(max_length=255, default='PROVA')
    file_referto = models.FileField(null=True)
    cda2 = models.TextField(null=True)
    



