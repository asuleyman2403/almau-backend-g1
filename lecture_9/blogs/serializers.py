from rest_framework import serializers
from blogs.models import Blog, Post


class BlogSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Blog
        fields = '__all__'
        # fields = ('id', 'title',)
        # fields = ['id', 'title']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

