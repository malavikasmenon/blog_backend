from django.db import models
from model_utils.fields import StatusField
from model_utils import Choices

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=120)
    subtitle = models.CharField(max_length=500, null=True, blank=True)
    content = models.TextField()
    image_url = models.TextField()
    year_of_release = models.CharField(max_length=4, null=True, blank=True)
    POST_CHOICES = Choices('movies', 'shows', 'books')
    post_type = StatusField(choices_name='POST_CHOICES')
    created = models.DateTimeField(auto_now_add=True)
    tags = models.TextField()
    slug_field = models.CharField(max_length=120)

    def __str__(self):
        return self.title
