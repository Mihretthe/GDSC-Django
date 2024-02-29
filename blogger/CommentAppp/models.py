from django.db import models
from django.utils import timezone
from blog.models import Post

# Create your models here.

class Comment(models.Model):
    content = models.TextField(max_length = 250)
    author = models.CharField(max_length = 250)
    published_date = models.DateTimeField(default = timezone)
    post = models.ForeignKey(Post, on_delete = models.CASCADE)