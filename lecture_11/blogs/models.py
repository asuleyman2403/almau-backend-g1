from django.db import models
from my_auth.models import User


class Blog(models.Model):
    title = models.CharField(null=False, blank=False, max_length=255)
    description = models.TextField(null=False, blank='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, null=False, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blog'


class Post(models.Model):
    title = models.CharField(null=False, blank=False, max_length=255)
    content = models.TextField(null=False, blank='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='posts')

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
