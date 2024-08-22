from rest_framework.permissions import BasePermission
from coments.models import Comment

class IsOwnerOrReadAndCreateOnly(BasePermission):

    def has_permission(self, request, view):

        if request.method == 'GET' or request.method == 'POST':
            return True
        else:
            #Sacando el id del comentario
            id_comment = view.kwargs['pk']
            comment = Comment.objects.get(pk=id_comment)

            #Obteniendo id del usuario
            id_user = request.user.pk
            #id deel usuario del comentario
            id_user_comment = comment.user_id


            if id_user == id_user_comment:
                return True
            else:
                return False