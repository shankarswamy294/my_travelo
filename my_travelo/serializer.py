"""
from my_travelo.models import Upload,User
from rest_framework import serializers
class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name','location')

class TodeItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upload
        fields = ('pic','desciption','name')

"""

