from django.shortcuts import render
from rest_framework import viewsets
from .models import Link
from .serializers import LinkSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny


# class LinkViewSet(viewsets.ModelViewSet):
#     queryset=Link.objects.all()
#     serializer_class = LinkSerializer

class PostListApi(generics.ListAPIView):
    queryset=Link.objects.filter(active=True)
    serializer_class = LinkSerializer
class PostCreateApi(generics.CreateAPIView):
    queryset=Link.objects.filter(active=True)
    serializer_class = LinkSerializer
class PostDetailApi(generics.RetrieveAPIView):
    queryset=Link.objects.filter(active=True)
    serializer_class = LinkSerializer
class PostUpdateApi(generics.UpdateAPIView):
    queryset=Link.objects.filter(active=True)
    serializer_class = LinkSerializer
class PostDeleteApi(generics.DestroyAPIView):
    queryset=Link.objects.filter(active=True)
    serializer_class = LinkSerializer
