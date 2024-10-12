from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from django.http.response import JsonResponse, Http404, HttpResponseNotFound
from library.models import Autor, Libro
from library.serializers import AutorSerializer, LibroSerializer

# AUTOR VIEWS
class AutorView(generics.ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'nombre':['contains'],
        'apellido':['contains'],
        'fecha_nacimiento':['contains'],        
    }


class AutorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer


# LIBRO VIEWS
class LibroView(generics.ListCreateAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'titulo':['contains'],
        'fecha_publicacion':['contains'],
    }


class LibroDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer