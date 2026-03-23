from rest_framework import viewsets
from rest_framework import mixins

from .models import Cat, Owner
from .serializers import CatSerializer, OwnerSerializer


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer


class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

class CreateRetrieveViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                            viewsets.GenericViewSet):
    pass

class LightCatViewSet(CreateRetrieveViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer