from rest_framework import serializers
from .models import Filme, Diretor

class DiretorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diretor
        fields = '__all__'

class FilmeSerializer(serializers.ModelSerializer):
    diretor = DiretorSerializer()
    
    class Meta:
        model = Filme
        fields = '__all__'