from api.models import Example

from rest_framework import serializers


class ExampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Example
        fields = "__all__"
