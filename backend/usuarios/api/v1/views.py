from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegistroUsuarioSerializer


class RegistroUserView(APIView):
    def post(self, request):
        serializer = RegistroUsuarioSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'mensaje': 'Usuario registrado correctamente'}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)