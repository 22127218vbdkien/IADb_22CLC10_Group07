from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Set length of titles
MAXLEN_TITLE = 150
MAXLEN_LINK = 150

class Anime(models.Model):
    FormatType = models.TextChoices('FormatType', 'TV TV_SHORT MOVIE SPECIAL OVA ONA MUSIC')
    StatusType = models.TextChoices('StatusType', 'FINISHED RELEASING NOT_YET_RELEASED CANCELLED HIATUS')
    SourceType = models.TextChoices('SourceType',
        'ORIGINAL MANGA LIGHT_NOVEL VISUAL_NOVEL VIDEO_GAME OTHER NOVEL DOUJINSHI ANIME WEB_NOVEL LIVE_ACTION GAME COMIC MULTIMEDIA_PROJECT PICTURE_BOOK'
    )

    # Primary key
    id = models.AutoField(primary_key=True)
    # The anilist id of the anime
    id_anilist = models.IntegerField(unique=True)
    # The mal id of the anime
    id_mal = models.IntegerField(unique=True)
    # The romanization of the native language title
    romaji_title = models.CharField(max_length=MAXLEN_TITLE, unique=True)
    # The official english title
    english_title = models.CharField(max_length=MAXLEN_TITLE, unique=True)
    # Official title in it's native language
    native_title = models.CharField(max_length=MAXLEN_TITLE, unique=True)
    # The format the media was released in
    format = models.CharField(choices=FormatType, max_length=10)
    # The current releasing status of the media
    status = models.CharField(choices=StatusType, max_length=20)
    # Short description of the media's story and characters
    description = models.TextField()
    # The first official release date of the media
    start_date = models.DateTimeField()
    # The last official release date of the media
    end_date = models.DateTimeField()
    # The amount of episodes the anime has when complete
    episodes = models.SmallIntegerField()
    # The general length of each anime episode in minutes
    duration = models.SmallIntegerField()
    # Source type the media was adapted from
    source = models.CharField(choices=SourceType, max_length=20)
    # Official Twitter hashtags for the media
    hashtag = models.CharField(max_length=MAXLEN_LINK)
    # Media trailer or advertisement
    trailer = models.CharField(max_length=MAXLEN_LINK)
    # The cover images of the media
    cover_img_large = models.CharField(max_length=MAXLEN_LINK)
    cover_img_med = models.CharField(max_length=MAXLEN_LINK)
    # The banner image of the media
    banner_img_large = models.CharField(max_length=MAXLEN_LINK)
    banner_img_med = models.CharField(max_length=MAXLEN_LINK)
    # A weighted average score of all the user's scores of the media
    weighted_score = models.SmallIntegerField()
    # Mean score of all the user's scores of the media
    mean_score = models.SmallIntegerField()
    # The number of users with the media on their list
    popularity = models.IntegerField()
    # The amount of related activity in the past day (may change time period)
    trending = models.BigIntegerField()
    # The amount of user's who have favourited the anime
    favorites = models.IntegerField()

    # ManyToMany
    studios = models.ManyToManyField('Studio', through='AnimeProducedByStudio', blank=True)
    staffs = models.ManyToManyField('Staff', through='StaffInAnime', blank=True)
    tags = models.ManyToManyField('Tag', through='AnimeTag', blank=True)
    relations = models.ManyToManyField('Anime', through='AnimeRelation', blank=True)

class AnimeSynonym(models.Model):
    anime_id = models.ForeignKey('Anime', on_delete=models.CASCADE)
    synonym = models.CharField(max_length=MAXLEN_TITLE, unique=True)

class Studio(models.Model):
    # Primary key
    id = models.AutoField(primary_key=True)
    # The name of the studio
    name = models.CharField(max_length=MAXLEN_TITLE, unique=True)
    # The amount of user's who have favourited the studio
    favorites = models.IntegerField()

class Character(models.Model):
    # Primary key
    id = models.AutoField(primary_key=True)
    # The character's full name
    name = models.CharField(max_length=MAXLEN_TITLE)
    # The character's full name in their native language
    name_native = models.CharField(max_length=MAXLEN_TITLE)
    # Character images
    img_large = models.CharField(max_length=MAXLEN_LINK)
    img_med = models.CharField(max_length=MAXLEN_LINK)
    # A general description of the character
    description = models.TextField()
    # The character's gender. Usually Male, Female, or Non-binary but can be any string.
    gender = models.CharField(max_length=50)
    # The character's birth date
    date_of_birth = models.DateField()
    # The character's age. Note this is a string, not an int, it may contain further text and additional ages.
    age = models.TextField()
    # The amount of user's who have favourited the character
    favorites = models.IntegerField()

class Staff(models.Model):
    # Primary key
    id = models.AutoField(primary_key=True)
    # The person's full name
    name = models.CharField(max_length=MAXLEN_TITLE)
    # The person's full name in their native language
    name_native = models.CharField(max_length=MAXLEN_TITLE)
    # The person's images
    img_large = models.CharField(max_length=MAXLEN_LINK)
    img_med = models.CharField(max_length=MAXLEN_LINK)
    # A general description of the staff member
    description = models.TextField()
    # The staff's gender
    gender = models.CharField(max_length=50)
    # The staff's birth date
    date_of_birth = models.DateField()
    # The staff's age
    age = models.SmallIntegerField()
    # The persons birthplace or hometown
    home_town = models.CharField(max_length=MAXLEN_TITLE)

class StaffInAnime(models.Model):
    anime_id = models.ForeignKey('Anime', on_delete=models.CASCADE)
    staff_id = models.ForeignKey('Staff', on_delete=models.CASCADE)
    staff_role = models.CharField(max_length=150)

    class Meta:
        unique_together = [['anime_id', 'staff_id']]

    # ManyToMany

class StaffVoiceCharacter(models.Model):
    # A staff can optionally be a voice actor/actress
    staff_in_anime = models.OneToOneField('StaffInAnime', on_delete=models.CASCADE, unique=True, null=True)
    # The character ID
    char_id = models.ForeignKey('Character', on_delete=models.CASCADE)
    # The role of the character in that anime
    CharRoleType = models.TextChoices('CharRoleType', 'MAIN SUPPORTING BACKGROUND')
    char_role = models.CharField(choices=CharRoleType, max_length=10)

    class Meta:
        unique_together = [['char_id', 'staff_in_anime_id']]

class AnimeProducedByStudio(models.Model):
    anime_id = models.ForeignKey('Anime', on_delete=models.CASCADE)
    studio_id = models.ForeignKey('Studio', on_delete=models.CASCADE)

    class Meta:
        unique_together = [['anime_id', 'studio_id']]

class AnimeRelation(models.Model):
    RelationType = models.TextChoices('RelationType',
        'SEQUEL PARENT SIDE_STORY CHARACTER SUMMARY SPIN_OFF OTHER COMPILATION CONTAINS'
    )

    anime_id = models.ForeignKey('Anime', on_delete=models.CASCADE, related_name='anime_id')
    senior_anime_id = models.ForeignKey('Anime', on_delete=models.CASCADE, related_name='senior_anime_id')
    relation = models.CharField(choices=RelationType, max_length=15)

    class Meta:
        unique_together = [['anime_id', 'senior_anime_id']]

class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, unique=True)
    description = models.TextField()
    category = models.CharField(max_length=150)
    is_general_spoiler = models.BooleanField(default=False)

class AnimeTag(models.Model):
    anime_id = models.ForeignKey('Anime', on_delete=models.CASCADE)
    tag_id = models.ForeignKey('Tag', on_delete=models.CASCADE)
    rank = models.SmallIntegerField(default=0)
    is_spoiler = models.BooleanField(default=False)

    class Meta:
        unique_together = [['anime_id', 'tag_id']]

class ExternalSite(models.Model):
    # Primary key
    id = models.AutoField(primary_key=True)
    # The name of the site
    name = models.CharField(max_length=MAXLEN_TITLE, unique=True)
    # The link to the icon of the site
    icon = models.CharField(max_length=MAXLEN_LINK)
    # The native language of the content on that site
    language = models.CharField(max_length=50)

class AnimeExternalLink(models.Model):
    anime_id = models.ForeignKey('Anime', on_delete=models.CASCADE)
    url = models.CharField(max_length=MAXLEN_LINK, unique=True)
    site_id = models.ForeignKey('ExternalSite', null=True, on_delete=models.SET_NULL)

class StaffExternalLink(models.Model):
    staff_id = models.ForeignKey('Staff', on_delete=models.CASCADE)
    url = models.CharField(max_length=MAXLEN_LINK, unique=True)
    site_id = models.ForeignKey('ExternalSite', null=True, on_delete=models.SET_NULL)
