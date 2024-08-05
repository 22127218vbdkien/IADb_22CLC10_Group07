from typing import Any
from django.contrib.auth.models import User
from django.db import models
from base.models import *
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Avg


class FavoriteCharacter(models.Model):
    user_id = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    char_id = models.ForeignKey('base.Character', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        character = Character.objects.get(id=self.char_id.id)
        character.favorites += 1
        character.save()

    def delete(self, *args, **kwargs):
        character = Character.objects.get(id=self.char_id.id)
        character.favorites -= 1
        character.save()
        super().delete(*args, **kwargs)

    class Meta:
        unique_together = [['user_id', 'char_id']]

class FavoriteStudio(models.Model):
    user_id = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    studio_id = models.ForeignKey('base.Studio', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        studio = Studio.objects.get(id=self.studio_id.id)
        studio.favorites += 1
        studio.save()

    def delete(self, *args, **kwargs):
        studio = Studio.objects.get(id=self.studio_id.id)
        studio.favorites -= 1
        studio.save()
        super().delete(*args, **kwargs)

    class Meta:
        unique_together = [['user_id', 'studio_id']]

class FavoriteStaff(models.Model):
    user_id = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    staff_id = models.ForeignKey('base.Staff', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        staff = Staff.objects.get(id=self.staff_id.id)
        staff.favorites += 1
        staff.save()

    def delete(self, *args, **kwargs):
        staff = Staff.objects.get(id=self.staff_id.id)
        staff.favorites -= 1
        staff.save()
        super().delete(*args, **kwargs)

    class Meta:
        unique_together = [['user_id', 'staff_id']]

class AnimeInCollection(models.Model):
    ListType = models.TextChoices('ListType', 'WATCHING COMPLETED PAUSED DROPPED PLANNING')

    user_id = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    anime_id = models.ForeignKey('base.Anime', on_delete=models.CASCADE)
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

    def save(self, *args, **kwargs):
        existed = AnimeInCollection.objects.filter(id=self.id).exists()
        if existed:
            pre_save = AnimeInCollection.objects.get(id=self.id)
            pre_favorite = pre_save.is_favorite
        else:
            pre_favorite = 0

        super().save(*args, **kwargs)

        anime = Anime.objects.get(id=self.anime_id.id)
        if (self.is_favorite - pre_favorite == 1):
            anime.favorites += 1
        elif (self.is_favorite - pre_favorite == -1):
            anime.favorites -= 1
        if not existed:
            anime.popularity += 1
        anime.mean_score = AnimeInCollection.objects.aggregate(Avg('score', default=0))['score__avg']
        anime.save()

    def delete(self, *args, **kwargs):
        pre_del = AnimeInCollection.objects.get(id=self.id)
        anime = Anime.objects.get(id=self.anime_id.id)
        if (pre_del.is_favorite == True):
            anime.favorites -= 1
        super().delete(*args, **kwargs)
        anime.mean_score = AnimeInCollection.objects.aggregate(Avg('score', default=0))['score__avg']
        anime.save()

    class Meta:
        unique_together = [['user_id', 'anime_id']]