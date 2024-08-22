from rest_framework import serializers

#Modelos
from posts.models import Post
from users.api.serializers import UserSerializer
from categories.api.serializers import CategorySerializer

#
class PostSerializer(serializers.ModelSerializer):

    #Propiedad user devuelva todos los valores del usuario
    user = UserSerializer()
    #Propiedad que devuelve todos los valores de la categoria
    category = CategorySerializer()

    class Meta:
        model = Post
        fields = ['title','content','slug','miniature','created_at','published','user','category']





        