import datetime
# Create your views here.
from django.http import HttpResponse, JsonResponse
from gestionale.models import Esame

""" crea un campo per dichiarare la variabile creato in models"""
def index(request):
    esame = Esame()

    esame.data_ora = datetime.datetime.now()
    esame.tipo = 'test'
    esame.esito = 'esito2'
    esame.struttura = 'struttura3'
    esame.save()

    return HttpResponse("Hello, world. You're at the polls.")

""" per recuperare dati da database"""
def index2(request): 
    esami = Esame.objects.all()
    result = []
    for esame in esami:
        result.append({ 
            'data_ora':str(esame.data_ora),
            'tipo': esame.tipo,})
            
    return JsonResponse(result, safe=False)