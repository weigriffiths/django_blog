from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
# What do we want to save to database?

# models.CASCADE will delete all posts by user that becomes deleted
# default = timezone.now will publish time of post, but also any modification time

class Post(models.Model):
  title = models.CharField(max_length=100)
  content = models.TextField()
  date_posted = models.DateTimeField(default=timezone.now)
  author = models.ForeignKey(User, on_delete=models.CASCADE)

  class Meta:
    ordering = ['-date_posted']

  def __str__(self):
    return self.title
  
  # Tell Django where to find the location of specific posts
  def get_absolute_url(self):
    return reverse('post-detail', kwargs={'pk': self.pk})