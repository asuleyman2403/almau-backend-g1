from rest_framework.decorators import api_view
from rest_framework.views import Response
from rest_framework import status
from blogs.serializers import BlogSerializer, PostSerializer
from blogs.models import Blog, Post
from datetime import datetime


@api_view(['GET', 'POST'])
def list_create_blog(request):
    if request.method == 'GET':
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        data = request.data
        data['created_at'] = datetime.now()
        serializer = BlogSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)

