from luizalabs.consuming_facebook.models import Person
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = ('id', 'username', 'name', 'facebook_id', 'gender')

    # def save(self):
    #     p = Person()
    #     p.name = 'teste'
    #     p.save()
