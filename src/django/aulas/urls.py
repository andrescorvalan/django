from django.urls import path
from .views import hello,bye,edad,primer_plantilla,segunda_plantilla,tercer_plantilla,cuarta_plantilla,crear_musico,crear_album

urlpatterns = [
    path('hello', hello),
    path('bye', bye),
    path('edad/<int:anios>/<int:futuro>', edad),
    path('plantilla1/', primer_plantilla),
    path('plantilla2/', segunda_plantilla),
    path('plantilla3/', tercer_plantilla),
    path('plantilla4/', cuarta_plantilla),
    path('crearmusico/<nombre>/<apellido>/<instrumento>', crear_musico),
    path('crearalbum/<nombre>/<int:estrellas>/<int:id>', crear_album),

]

