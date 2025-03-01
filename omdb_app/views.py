import requests
from django.conf import settings
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Filme, Diretor
from .serializers import FilmeSerializer, DiretorSerializer

from rest_framework import viewsets
from .models import Diretor
from .serializers import DiretorSerializer

class DiretorViewSet(viewsets.ModelViewSet):
    queryset = Diretor.objects.all()
    serializer_class = DiretorSerializer

class FilmeViewSet(viewsets.ModelViewSet):
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer

    @action(detail=False, methods=['get'])
    def fetch_from_omdb(self, request):
        titulo = request.query_params.get('title')
        if titulo:
            api_key = settings.OMDB_API_KEY
            try:
                response = requests.get(f'http://www.omdbapi.com/?t={titulo}&apikey={api_key}')
                response.raise_for_status() 
                data = response.json()
                
                if data.get("Response") == "False":
                    return Response({"error": "Filme não encontrado na API OMDB."}, status=404)
                
                
                director_name = data.get("Director")
                diretor = Diretor.objects.filter(nomeDiretor__icontains=director_name).first()
                if diretor:
                    data["DirectorInfo"] = {
                        "nomeDiretor": diretor.nomeDiretor,
                        "idade": diretor.idade
                    }
                else:
                    data["DirectorInfo"] = "Diretor não encontrado no banco de dados."
                return Response(data)
            except requests.exceptions.RequestException as e:
                return Response({"error": f"Erro na requisição da API: {str(e)}"}, status=500)
        else:
            return Response({"error": "Título do filme não fornecido."}, status=400)