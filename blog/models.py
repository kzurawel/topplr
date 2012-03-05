from django.db import models
from model_utils.managers import InheritanceManager

# Create your models here.
class Tag(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)

    def __unicode__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField("date published")
    summary = models.TextField(null=True, blank=True)
    main_content = models.TextField(null=True, blank=True)
    related_posts = models.ManyToManyField("self", null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True, null=True, related_name='posts')

    objects = InheritanceManager()

    def __unicode__(self):
        return self.title

class NewsPost(Post):
    class Meta:
        verbose_name = "News post"

    def post_type(self):
        return "standard"

class VideoPost(Post):
    vid_caption = models.CharField(max_length=255)
    video_url = models.URLField("Video URL")

    class Meta:
        verbose_name = "Video post"

    def post_type(self):
        return "video"

class PhotoPost(Post):
    photo_caption = models.CharField(max_length=255, null=True, blank=True)
    photo = models.FileField(upload_to="photos")
    photo_location = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = "Photo post"

    def post_type(self):
        return "image"

class QuotePost(Post):
    quote_author = models.CharField(max_length=255)
    quote_date = models.DateField(null=True, blank=True)
    quote_source = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = "Quote post"

    def post_type(self):
        return "quote"
