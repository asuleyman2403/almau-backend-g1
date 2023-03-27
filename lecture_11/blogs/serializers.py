from rest_framework import serializers
from blogs.models import Blog, Post
from my_auth.serializers import UserSerializer


class BlogSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    owner_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Blog
        fields = '__all__'
        # fields = ('id', 'title',)
        # fields = ['id', 'title']


class PostSerializer(serializers.ModelSerializer):
    blog = BlogSerializer(read_only=True)
    blog_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Post
        fields = '__all__'

