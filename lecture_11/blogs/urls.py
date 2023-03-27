from django.urls import path
from blogs.views.cbv import ListCreateBlogAPIView, RetrieveUpdateDestroyAPIView
from blogs.views.generics import ListPostAPIView, CreatePostAPIView, PostsAPIView, RetrievePostAPIView, \
    UpdatePostAPIView, DeletePostAPIView, PostAPIView, BlogsPostsAPIView

urlpatterns = [
    path('blogs', ListCreateBlogAPIView.as_view()),
    path('blogs/<int:pk>', RetrieveUpdateDestroyAPIView.as_view()),
    path('blogs/<int:pk>/posts/', BlogsPostsAPIView.as_view()),
    path('posts/', PostsAPIView.as_view()),
    path('posts/<int:pk>/', PostAPIView.as_view())
]
