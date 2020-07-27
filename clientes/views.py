from rest_framework import viewsets, filters
from clientes.serializers import ClienteSerializer
from clientes.models import Cliente
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

class ClientesViewSet(viewsets.ModelViewSet):
    """Listando todos os clientes"""
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['nome', 'email', 'cpf', 'rg', 'ativo']
    search_fields = ['nome', 'cpf']
    ordering_fields = ['nome']

class BuscaClientePorCPF(generics.ListAPIView):
    """Verifica se o CPF está cadastrado e se é um cliente"""
    serializer_class = ClienteSerializer
    def get_queryset(self):
        cpf = self.kwargs['cpf']
        return Cliente.objects.filter(cpf=cpf)