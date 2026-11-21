"""Utilitaires partagés par les vues de consultation."""

from rest_framework.exceptions import ValidationError
from rest_framework.response import Response


def list_response(queryset, serializer_class):
    """Sérialise une collection Django dans une réponse JSON."""
    return Response(serializer_class(queryset, many=True).data)


def paginated_list_response(queryset, serializer_class, request):
    """Retourne une page stable de résultats et son total calculé par la base."""
    try:
        page = int(request.query_params.get("page", 1))
        page_size = int(request.query_params.get("page_size", 15))
    except ValueError as error:
        raise ValidationError("page et page_size doivent être des entiers.") from error

    if page < 1:
        raise ValidationError({"page": "Doit être supérieur ou égal à 1."})
    if not 1 <= page_size <= 100:
        raise ValidationError({"page_size": "Doit être compris entre 1 et 100."})

    count = queryset.count()
    start = (page - 1) * page_size
    results = serializer_class(queryset[start:start + page_size], many=True).data
    return Response({
        "count": count,
        "page": page,
        "page_size": page_size,
        "results": results,
    })
