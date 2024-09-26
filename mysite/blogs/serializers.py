from rest_framework import serializers
from .models import Blog
from users.models import CustomUser

class CreateBlogSerializer(serializers.ModelSerializer):

    title = serializers.CharField(max_length=100, min_length=2)

    class Meta:
        model = Blog
        fields = ('title', 'caption', 'media', 'user')

class FetchBlogSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()  # To display user details in the response

    class Meta:
        model = Blog
        fields = '__all__'
