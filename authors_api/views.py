from django.shortcuts import render
from authors_api import models, serializers, permissions
from rest_framework import viewsets
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

class AuthorViewset(viewsets.ModelViewSet):

    serializer_class = serializers.AuthorsSerializer
    queryset = models.User.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)