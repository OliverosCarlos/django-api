from rest_framework import serializers
from library.models import Autor, Libro

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = (  'id',
                    'nombre',
                    'apellido',
                    'fecha_nacimiento'
                    )
        

class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = (  'id',
                    'titulo',
                    'fecha_publicacion',
                    'autor',
                    )