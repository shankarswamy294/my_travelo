from rest_framework import serializers
from my_travelo.models import Upload,User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pic','name','location_from')


class UploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upload
        fields = ('pic','description','name')