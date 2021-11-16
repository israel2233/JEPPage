from django.contrib import admin
from contactos.models import Personas
from contactos.models import TelefonoPersona
from contactos.models import CorreoPersona
# Register your models here.
admin.site.register(Personas)
admin.site.register(TelefonoPersona)
admin.site.register(CorreoPersona)

