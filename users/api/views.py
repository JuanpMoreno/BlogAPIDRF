from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from users.models import User

from .serializers import UserRegisterSerializer, UserSerializer, UserUpdateSerializer

#Vista para registrar usuario
class RegisterView(APIView):
    
    def post(self, request):
        #Datos necesarios para registrar el usuario
        serializer = UserRegisterSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
        return Response(status=status.HTTP_200_OK, data='Todo Ok')
    

#Vista que mostrara todos los datos del usuario logueado
class UserView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
    

    #Actualizar datos del usuario
    def put(self, request):
        user = User.objects.get(id=request.user.id)
        serializer = UserUpdateSerializer(user, request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)