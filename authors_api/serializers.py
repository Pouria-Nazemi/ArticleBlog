from rest_framework import serializers
from authors_api import models

class AuthorsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = ['id', 'username','last_name', 'email', 'blog', 'password']
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

class ArticlesSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Article
        fields = ['id', 'title', 'description', 'link', 'date_modified', 'subject', 'author_id']
        extra_kwargs = {
            'author_id': {
                'read_only': True,
            }
        }