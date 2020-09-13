from rest_framework import serializers
from parliment_api.models import Parliment


class MPSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parliment
        fields = ('__all__')
