from rest_framework import serializers

from .models import Post

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'subtitle', 'content', 'post_type', 'year_of_release', 'created', 'tags', 'image_url', 'slug_field']