from rest_framework import generics

from user.serializer import UserSerializer


class CreateUserViwew(generics.CreateAPIView):
    serializer_class= UserSerializer