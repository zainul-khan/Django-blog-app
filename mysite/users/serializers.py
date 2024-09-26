from rest_framework import serializers
from django.contrib.auth import get_user_model
# from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import make_password

User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=12, min_length=5)

    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }


    def create(self, validated_data):
        hashed_password = make_password(validated_data['password'])
        validated_data['password'] = hashed_password
        user = User(**validated_data)
        user.save()
        return user
