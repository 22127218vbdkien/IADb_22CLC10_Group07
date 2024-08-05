from django.contrib.auth.models import User
from django.db import models
from base.models import *


class Thread(models.Model):
    owner_id = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    body = models.TextField()
    view_count = models.BigIntegerField(default=0)
    comment_count = models.BigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    thread_id = models.ForeignKey('Thread', on_delete=models.CASCADE)
    user_id = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    reply_to = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, related_name='reply_to')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)