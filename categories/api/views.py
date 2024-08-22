from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

#Modelos
from categories.models import Category

#serializadores
from .serializers import CategorySerializer

#permisos
from categories.api.permissions import IsAdminOrReadOnly


#Vista
class CategoryAPIViewSet(ModelViewSet):
    permission_class = [IsAdminOrReadOnly]
    serializer_class = CategorySerializer
    #Trae todos los registros de categorias
    queryset = Category.objects.all()

    #Trae las categorias de acuerdo a un filtro en especifico.
    #queryset = Category.objects.filter(published=True)

    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['published']
