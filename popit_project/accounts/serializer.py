from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','profile_image','login_id','nickname','email', 'password', 're_password', 'alarm')
        read_only_fields = ('id'),


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        #fields = '__all__'
        fields = ('id','profile_image','login_id','nickname','email', 'password', 're_password', 'alarm')
    
    def create(self, validated_data):
        login_id = validated_data.get('login_id')
        email = validated_data.get('email')
        #password = validated_data.get('re_password')
        nickname = validated_data.get('nickname')
        #profile_image = validated_data.get('profile_image')

        re_password = validated_data.get('re_password')

        #if re_password == password:
        user = User(
            login_id=login_id,
            email=email,
            nickname = nickname,
            re_password = re_password
            #profile_image = profile_image
        )
        user.set_password(re_password)
        user.save()
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'