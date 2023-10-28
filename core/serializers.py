from rest_framework import serializers
from .models import *


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields= ['username','password']

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields= ['username','password']

class Profileserializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class FollowersSerializer(serializers.ModelSerializer):
    class Meta:
        model = FollowersCount
        fields = '__all__'



    