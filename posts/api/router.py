from rest_framework.routers import DefaultRouter

#Vistas
from posts.api.views import PostAPIViewSet

router_posts = DefaultRouter()
router_posts.register(prefix='posts', basename='posts', viewset=PostAPIViewSet)
