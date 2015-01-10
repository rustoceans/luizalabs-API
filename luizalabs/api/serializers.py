from luizalabs.consuming_facebook.models import Person
from rest_framework import serializers
from rest_framework.pagination import *
from rest_framework import pagination


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = ('username', 'name', 'facebook_id', 'gender')


class PaginatedUserSerializer(pagination.PaginationSerializer):

    """
    Serializes page objects of user querysets.
    """
    class Meta:
        object_serializer_class = UserSerializer
