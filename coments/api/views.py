from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

#Modelos
from coments.models import Comment

#serializadores
from .serializers import CommentSerializer

#Permisos
from .permissions import IsOwnerOrReadAndCreateOnly

#vista
class CommentApiViewSet(ModelViewSet):

    permission_classes = [IsOwnerOrReadAndCreateOnly]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    #Por que campo quiero ordenar
    ordering = ['-created_at']
    #Por que campos puede filtrar
    filterset_fields = ['post']
