from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        #fields = '__all__'
        fields = ('id','profile_image','login_id','nickname','email', 'password', 're_password', 'alarm')
    
    def create(self, validated_data):
        login_id = validated_data.get('login_id')
        email = validated_data.get('email')
        password = validated_data.get('password')
        nickname = validated_data.get('nickname')
        profile_image = validated_data.get('profile_image')

        user = User(
            login_id=login_id,
            email=email,
            nickname = nickname,
            profile_image = profile_image
        )
        user.set_password(password)
        user.save()
        return user
 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'