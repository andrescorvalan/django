#from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render
from .models import Musician, Album
# Create your views here.

def hello(request):
    return HttpResponse("Hola Mundo")

def bye(request):
    return HttpResponse("Hasta Luego")

def edad(request,anios,futuro):
    incremento = futuro -  date.today().year
    cumpliras = anios + incremento
    mensaje ="En el año %d cumpliras %d años"%(futuro,cumpliras)
    return HttpResponse(mensaje)

def primer_plantilla(request):
    plantilla = """
        <html>
            <body>
                <h2>
                    Hola {{nombre}}, esta es mi primer plantilla
                </h2>
            </body>
        </html>
    """
    tpl = Template(plantilla)
    ctx = Context({'nombre':'Juan'})
    mensaje = tpl.render(ctx)
    return HttpResponse(mensaje)

def segunda_plantilla(request):
    tpl = get_template('segunda_plantilla.html')
    mensaje = tpl.render(
        {'nombre':'Jose',
        'fecha_actual': date.today()
        }
    )
    return HttpResponse(mensaje)

def tercer_plantilla(request):
    return render(request,"tercer_plantilla.html",{
        'nombre':'Pedro',
        'fecha_actual': date.today()
    })
class Empleado(object):
    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido


def cuarta_plantilla(request):
    laborables = ['Lunes','Martes','Miercoles','Jueves']
    return render(request,"cuarta_plantilla.html",{
        'empleado':Empleado('Andrés','Corvalan'),
        'fecha_actual': date.today(),
        'dias_laborables':laborables
    })



def crear_musico(request,nombre,apellido,instrumento):
    musico=Musician(first_name=nombre,last_name=apellido,instrument=instrumento)
    musico.save()
    mensaje="Músico %s %s creado correctamente con id %d"%(musico.first_name,musico.last_name,musico.id) 
    return HttpResponse(mensaje)

def crear_album(request,nombre,estrellas,id):
    musico=Musician.objects.get(id=id)
    album=Album(name=nombre,release_date=date.today(),num_stars=estrellas,artist=musico)
    album.save()
    mensaje="Se creo el album %s del artista %s con id %d"%(album.name,musico.first_name,album.id)

    return HttpResponse(mensaje)