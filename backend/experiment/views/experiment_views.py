from rest_framework import generics, viewsets
from experiment.models import Experiment

from rest_framework import serializers


class ExperimentSerializer(serializers.ModelSerializer):
    basic_model_name = serializers.SerializerMethodField()

    class Meta:
        model = Experiment
        fields = ['title', 'basic_model', 'training_way', 'devices', 'status', 'basic_model_name']
        read_only_fields = ('status', 'basic_model_name')

    def get_basic_model_name(self, obj):
        return obj.basic_model.name



class ExperimentViewSet(viewsets.ModelViewSet):
    queryset = Experiment.objects.all()
    serializer_class = ExperimentSerializer
    permission_classes = []


