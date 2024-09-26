from escola.models import Estudante, Curso, Matricula
from escola.serializers import EstudanteSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasEstudanteSerializer, ListaMatriculasCursoSerializer, EstudanteSerializerV2
from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.throttling import UserRateThrottle
from escola.throttles import MatriculaAnonRateThrottle
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class EstudanteViewSet(viewsets.ModelViewSet):
    """
    Descrição da View:
    - Lista Estudantes por 'id' e 'nome'
    Parâmetros:
    - Filtra os Estudantes pelo valor de 'nome'
    - Versionamento : Atualiza a versão do filtro de Estudante para 'nome' e 'cpf' 
    """
    queryset = Estudante.objects.all().order_by('id')
    #serializer_class = EstudanteSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome', 'cpf']
    
    def get_serializer_class(self):
        if self.request.version == 'V2':
            return EstudanteSerializerV2
        return EstudanteSerializer
        
class CursoViewSet(viewsets.ModelViewSet):
    """
    Descrição da View:
    - Lista Curso por 'id'
    Parâmetros:
    - Filtra Curso pelo valor de 'id'
    """
    queryset = Curso.objects.all().order_by('id')
    serializer_class = CursoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
class MatriculaViewSet(viewsets.ModelViewSet):
    """
    Descrição da View:
    - Lista Matriculas por 'id'
    Parâmetros:
    - Filtra Matriculas pelo valor de 'id' com metodos de 'get' e 'post'
    """
    queryset = Matricula.objects.all().order_by('id')
    serializer_class = MatriculaSerializer
    throttle_classes = [UserRateThrottle, MatriculaAnonRateThrottle]
    http_method_names = ["get", "post"]
    
class ListaMatriculaEstudante(generics.ListAPIView):
    """
    Descrição da View:
    - Lista Matriculas por id de Estudante
    Parâmetros:
    - pk (int): O identificador primário do objeto. Deve ser um número inteiro.
    """
    def get_queryset(self):
        queryset = Matricula.objects.filter(estudante_id = self.kwargs['pk']).order_by("id")
        return queryset
    serializer_class = ListaMatriculasEstudanteSerializer
    
class ListaMatriculaCurso(generics.ListAPIView):
    """
    Descrição da View:
    - Lista Matriculas por id de Curso
    Parâmetros:
    - pk (int): O identificador primário do objeto. Deve ser um número inteiro.
    """
    def get_queryset(self):
        queryset = Curso.objects.filter(curso_id = self.kwargs['pk']).order_by("id")
        return queryset
    serializer_class = ListaMatriculasCursoSerializer
