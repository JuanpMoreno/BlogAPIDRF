from rest_framework import serializers
from coments.models import Comment

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['content', 'created_at','user','post']