from django.shortcuts import render
from rest_framework import generics, permissions
from .permissions import IsOwner
from .serializers import BlogSerializer
from .models import BlogList


# Create your views here.
class CreateView(generics.ListCreateAPIView):
    """
    The class will list all POST method handlers
    """
    queryset = BlogList.objects.all()
    serializer_class = BlogSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)

    def create_blog(self, serializer):
        serializer.save(owner=self.request.user)


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset=BlogList.objects.all()
    serializer_class=BlogSerializer
    permission_classes=(permissions.IsAuthenticated,IsOwner)