from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import viewsets, status
from django_filters import rest_framework as filters
import datetime
from rest_framework.parsers import JSONParser,ParseError



from .serializers import BlogPostSerializer
from .models import Post
from .filters import BlogCategoryFilter

class BlogListView(viewsets.ReadOnlyModelViewSet):
    permission_classes = (AllowAny,)
    filter_backends = {filters.DjangoFilterBackend, }
    filterset_class = BlogCategoryFilter
    # filterset_fields = ('post_type')
    queryset = Post.objects.all()
    serializer_class = BlogPostSerializer

class BlogAddView(APIView):
    queryset = Post.objects.all()
    serializer_class = BlogPostSerializer
    def get(self, request):
        posts = Post.objects.all()
        serializer = BlogPostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = {
            'title': request.data.get('title'),
            'subtitle': request.data.get('subtitle'),
            'content': request.data.get('content'),
            'image_url': request.data.get('image_url'),
            'post_type': request.data.get('post_type'),
            'year_of_release': request.data.get('year_of_release'),
            # 'created': request.data.get('created'),
            'tags': request.data.get('tags'),
            'slug_field': request.data.get('slug_field')
        }
        serializer = BlogPostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status":"success",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                "status":"error",
                "data": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

