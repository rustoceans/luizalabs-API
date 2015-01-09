from django.shortcuts import render

# Create your views here.

from luizalabs.consuming_facebook.models import Person
from django.http import Http404

from luizalabs.api.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from luizalabs.consuming_facebook.facebook_user import Consuming
from rest_framework import mixins


class PersonList(mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 generics.GenericAPIView):

    """
    List all users or create a new user.
    """

    queryset = Person.objects.all()
    serializer_class = UserSerializer
    paginate_by = 10
    paginate_by_param = 'limit'
    # Set MAX results per page
    max_paginate_by = 1

    def get(self, request, *args, **kwargs):
        # users = Person.objects.all()
        # serializer = UserSerializer(users, many=True)
        # return Response(serializer.data)
        return self.list(request, *args, **kwargs)

    def post(self, request, format=None):
        # Turning the QueryDict in mutable.
        post_fields = request.POST.copy()

        """
        When I try search element at return of cons.decode_users()['index']
        give me as follows error:

        'no json object could be decoded.'

        I tried to convert each item, but don't worked.

        So, in each iterable, I called:
            cons.decode()['index']

        """

        cons = Consuming(post_fields['facebook_id'])
        post_fields['username'] = cons.decode_users()['username']

        # First called
        cons = Consuming(post_fields['facebook_id'])

        post_fields.update({'name': cons.decode_users()['name']})

        # Second called
        cons = Consuming(post_fields['facebook_id'])

        post_fields.update({'gender': cons.decode_users()['gender']})

        serializer = UserSerializer(data=post_fields)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PersonDetail(APIView):

    """
    Retrieve, update or delete a user instance.
    """

    def get_object(self, facebook_id):
        try:
            return Person.objects.get(facebook_id=facebook_id)
        except Person.DoesNotExist:
            raise Http404

    def get(self, request, facebook_id, format=None):
        user = self.get_object(facebook_id)
        user = UserSerializer(user)
        return Response(user.data)

    def put(self, request, facebook_id, format=None):
        user = self.get_object(facebook_id)
        serializer = UserSerializer(user, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, facebook_id, format=None):
        user = self.get_object(facebook_id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
