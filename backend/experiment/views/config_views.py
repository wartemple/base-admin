from rest_framework import generics, viewsets
from experiment.models import ConfigTemplate

from rest_framework import serializers


class ConfigTemplateSerializer(serializers.ModelSerializer):

    class Meta:
        model = ConfigTemplate
        fields = ['name']



class ConfigTemplateViewSet(viewsets.ModelViewSet):
    queryset = ConfigTemplate.objects.all()
    serializer_class = ConfigTemplateSerializer
    permission_classes = []


