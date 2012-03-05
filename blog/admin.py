from django.contrib import admin
from blog.models import Tag, Post, NewsPost, VideoPost, PhotoPost, QuotePost
from tinymce.widgets import TinyMCE
from django.db import models

class TagAdmin(admin.ModelAdmin):
    pass

class NewsPostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 12}, )},
    }

    class Media:
        js = ['tiny_mce/tiny_mce.js']

class VideoPostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 12}, )},
    }

    class Media:
        js = ['tiny_mce/tiny_mce.js']

class PhotoPostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 12}, )},
    }

    class Media:
        js = ['tiny_mce/tiny_mce.js']

class QuotePostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 12}, )},
    }

    class Media:
        js = ['tiny_mce/tiny_mce.js']

admin.site.register(Tag, TagAdmin)
admin.site.register(NewsPost, NewsPostAdmin)
admin.site.register(VideoPost, VideoPostAdmin)
admin.site.register(PhotoPost, PhotoPostAdmin)
admin.site.register(QuotePost, QuotePostAdmin)
