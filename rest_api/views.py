from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from reserva.models import Reserva, Petshop
from rest_api.serializers import (
    AgendamentoModelSerializer,
    PetshopNestedModelSerializer,
)


class AgendamentoModelViewSet(ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = AgendamentoModelSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_fields = ["tamanho"]


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticatedOrReadOnly])
def ultimos_cadastros(request):
    ultimos_cadastros = Reserva.objects.order_by("-data")[:5]
    serializer = AgendamentoModelSerializer(ultimos_cadastros, many=True, context={'request':request})
    return Response({"ultimos_cadastros": serializer.data})


@api_view(["DELETE"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticatedOrReadOnly])
def excluir_registro(request, pk):
    try:
        registro = Reserva.objects.get(pk=pk)
    except Reserva.DoesNotExist:
        return Response(
            {"detail": "Registro não encontrado"}, status=status.HTTP_404_NOT_FOUND
        )
    if request.method == "DELETE":
        registro.delete()
        return Response(
            {"detail": "Registro excluído com sucesso"},
            status=status.HTTP_204_NO_CONTENT,
        )


class PetshopModelViewSet(ReadOnlyModelViewSet):
    queryset = Petshop.objects.all()
    serializer_class = PetshopNestedModelSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
