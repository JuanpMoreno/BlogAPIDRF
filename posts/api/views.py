from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

#Modelos
from posts.models import Post

#Serializadores
from posts.api.serializers import PostSerializer

#Permisos
from .permissions import IsAdminOrReader


#Vistas para hacer CRUD del modelo Posts
class PostAPIViewSet(ModelViewSet):

    permission_classes = [IsAdminOrReader]
    serializer_class = PostSerializer
    queryset= Post.objects.filter(published=True)
    lookup_field = 'slug'

    #vista para devolver todos los posts de una categoria
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'category__slug']


