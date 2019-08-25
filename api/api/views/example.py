from api.models import Example
from api.serializers import ExampleSerializer

from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny


@permission_classes((AllowAny,))
class ExampleViewSet(viewsets.ModelViewSet):
    """
        Retrieve all our examples.
    """

    queryset = Example.objects.all()
    serializer_class = ExampleSerializer
