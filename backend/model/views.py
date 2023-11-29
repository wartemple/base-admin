from django.shortcuts import render


# Create your views here.
class CLASSNAMEViewSet(viewsets.ModelViewSet):
    queryset = CLASSNAME.objects.all()
    serializer_class = CLASSNAMESerializer
    permission_classes = []


