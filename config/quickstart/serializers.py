from django.contrib.auth.models import User, Group
# from config.quickstart.models import Test
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

# class TestSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Test
#         fields = ('id')
