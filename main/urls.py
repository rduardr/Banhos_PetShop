from django.contrib import admin
from django.urls import path, include

from principal.views import inicio, contato

urlpatterns = [
    path("", inicio, name="inicio"),
    path("contato/", contato, name="contato"),
    path("reserva/", include("reserva.urls", namespace="reserva")),
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("api/", include("rest_api.urls", namespace="api")),
]
