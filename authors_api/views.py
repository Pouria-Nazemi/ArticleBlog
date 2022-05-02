from django.shortcuts import render
from authors_api import models, serializers, permissions
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class AuthorViewset(viewsets.ModelViewSet):

    serializer_class = serializers.AuthorsSerializer
    queryset = models.User.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)


class UserLoginApiView(ObtainAuthToken):
   renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class ArticleViewset(viewsets.ModelViewSet):

    serializer_class = serializers.ArticlesSerializer
    queryset = models.Article.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (
        permissions.UpdateOwnArticle,
        IsAuthenticatedOrReadOnly
    )

    def perform_create(self, serializer):
        serializer.save(author_id=self.request.user)
