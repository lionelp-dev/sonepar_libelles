"""Utilitaires partagés par les vues de consultation."""

from rest_framework.response import Response


def list_response(queryset, serializer_class):
    """Sérialise une collection Django dans une réponse JSON."""
    return Response(serializer_class(queryset, many=True).data)
