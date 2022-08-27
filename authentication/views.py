from django.shortcuts import render
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics,status

from .models import User
from .serializers import UserCreationSerailizer
from rest_framework.parsers import MultiPartParser, FormParser
# Create your views here.
def hello(request):
    return Response(data={"title":"Hello!"})

class UserCreateView(generics.GenericAPIView):

    serializer_class = UserCreationSerailizer

    def post(self, request):
        data = request.data

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def get_parsers(self):
        if getattr(self, 'swagger_fake_view', False):
            return []
        return super().get_parsers()          
