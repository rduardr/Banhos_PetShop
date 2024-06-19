from django.urls import path
from rest_framework.routers import SimpleRouter

from rest_api.views import (
    ultimos_cadastros,
    excluir_registro,
    AgendamentoModelViewSet,
    PetshopModelViewSet,
)

app_name = "rest_api"

router = SimpleRouter(trailing_slash=False)
router.register(
    "agendamento",
    AgendamentoModelViewSet,
)
router.register("petshop", PetshopModelViewSet)

urlpatterns = [
    path("ultimos_cadastros", ultimos_cadastros, name="ultimos_cadastros_api"),
    path("excluir_registro/<int:pk>/", excluir_registro, name="excluir_registro_api"),
]

urlpatterns += router.urls
