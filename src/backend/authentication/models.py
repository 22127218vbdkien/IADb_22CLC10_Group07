from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.OneToOneField(
        'auth.User', 
        on_delete=models.CASCADE, 
        related_name='profile'
    )
    about = models.TextField(null=True, blank=True)
    avatar = models.TextField(null=True, blank=True)

class Complaint(models.Model):
    ComplaintType = models.TextChoices('ComplaintType', 
        'CONTENT USER BUG FUNCTION OTHER'
    )

    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    complaint_type = models.CharField(max_length=10, choices=ComplaintType)
    complaint_target = models.CharField(max_length=150, null=True)
    complaint_msg = models.TextField()