from django_filters import rest_framework as filters

from .models import Post

class BlogCategoryFilter(filters.FilterSet):
    class Meta:
        model = Post
        fields = ['post_type']
