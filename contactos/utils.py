from contactos.models import Personas, TelefonoPersona, CorreoPersona

def devuelveTelefonosYCorreos(personaId):
    telefonos = TelefonoPersona.objects.filter(persona_id=personaId)
    correos = CorreoPersona.objects.filter(persona_id=personaId)

    listaTelefonos = []
    listaCorreos = []
    for telefono in telefonos:
        listaTelefonos.append(telefono.telefono)
    for correo in correos:
        listaCorreos.append(correo.email)
    correosString = ' / '.join(listaCorreos)
    telefonosString = ' / '.join(listaTelefonos)

    return {"correos": correosString,
            "telefonos": telefonosString}
