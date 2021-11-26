import datetime

from django.shortcuts import render
from contactos.models import Personas, TelefonoPersona, CorreoPersona
from contactos.utils import devuelveTelefonosYCorreos

# Create your views here.
def contactos(request):
    persona = Personas.objects.get(nombres='JEP')
    # telefonos = TelefonoPersona.objects.filter(persona_id=persona.id)
    # correos = CorreoPersona.objects.filter(persona_id=persona.id)
    datos = devuelveTelefonosYCorreos(persona.id)
    mensaje = {"persona": persona,
               "datos": datos}
    return render(request, "contactPage.html", mensaje)