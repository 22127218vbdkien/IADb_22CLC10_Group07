from django.contrib.auth.models import User
from django.db import models
from base.models import *
from django.core.validators import MaxValueValidator, MinValueValidator


class FavoriteCharacter(models.Model):
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    char_id = models.ForeignKey('Character', on_delete=models.CASCADE)

    class Meta:
        unique_together = [['user_id', 'char_id']]

class FavoriteStudio(models.Model):
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    studio_id = models.ForeignKey('Studio', on_delete=models.CASCADE)

    class Meta:
        unique_together = [['user_id', 'studio_id']]

class FavoriteStaff(models.Model):
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    staff_id = models.ForeignKey('Staff', on_delete=models.CASCADE)

    class Meta:
        unique_together = [['user_id', 'staff_id']]

class AnimeInCollection(models.Model):
    ListType = models.TextChoices('ListType', 'READING REREADING COMPLETED PAUSED DROPPED PLANNING')

    owner = models.ForeignKey('User', on_delete=models.CASCADE)
    anime_id = models.ForeignKey('Anime', on_delete=models.CASCADE)
    is_favorite = models.BooleanField(default=False)
    in_list = models.CharField(choices=ListType, max_length=10, null=True)
    score = models.SmallIntegerField(
        null=True, 
        validators=[MaxValueValidator(100), MinValueValidator(0)]
    )
    progress = models.SmallIntegerField(null=True)
    start_date = models.DateTimeField(auto_now_add=True)
    finish_date = models.DateTimeField(null=True)
    notes = models.TextField(null=True)

    class Meta:
        unique_together = [['user_id', 'anime_id']]