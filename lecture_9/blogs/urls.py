from django.urls import path
from blogs.views.fbv import list_create_blog
from blogs.views.cbv import ListCreateBlogAPIView, RetrieveUpdateDestroyAPIView

urlpatterns = [
    path('blogs', ListCreateBlogAPIView.as_view()),
    path('blogs/<int:pk>', RetrieveUpdateDestroyAPIView.as_view())
]
