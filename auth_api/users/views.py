from .models import User
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from users.serializers import UserSerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserDetail(generics.ListRetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all().filter(username=self.request.user)
