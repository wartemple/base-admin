from django.urls import path, include
from rest_framework.routers import DefaultRouter
from experiment.views import ExperimentViewSet, ConfigTemplateViewSet

router = DefaultRouter()
router.register(r'experiments', ExperimentViewSet, basename='your-model')
router.register(r'config_templates', ConfigTemplateViewSet, basename='config-template')

urlpatterns = [
    path('', include(router.urls)),
]

