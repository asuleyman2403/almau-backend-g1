from rest_framework.views import Response, APIView
from rest_framework import status
from blogs.serializers import BlogSerializer
from blogs.models import Blog


class ListCreateBlogAPIView(APIView):
    def get(self, request):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        data['owner_id'] = request.user.id
        serializer = BlogSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class RetrieveUpdateDestroyAPIView(APIView):
    def get_blog(self, id):
        try:
            return Blog.objects.get(id=id)
        except Blog.DoesNotExist:
            return None

    def get(self, request, pk):
        blog = self.get_blog(pk)
        if blog is None:
            return Response({'message': 'Blog not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = BlogSerializer(blog)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        blog = self.get_blog(pk)
        data = request.data
        data['owner_id'] = request.user.id
        serializer = BlogSerializer(data=data, instance=blog)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        blog = self.get_blog(pk)
        if blog is None:
            return Response({'message': 'Blog not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            blog.delete()
            return Response({'message': 'Blog is deleted!'}, status=status.HTTP_200_OK)






