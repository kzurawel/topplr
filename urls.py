from django.conf.urls.defaults import patterns, include, url
from blog.views import PostListView
from blog.models import Post, NewsPost, PhotoPost, VideoPost, QuotePost, Tag

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', PostListView.as_view(model=Post)),
    url(r'^news/?', PostListView.as_view(model=NewsPost, queryset=NewsPost.objects.all(), template_name="blog/post_list.html")),
    url(r'^photos/?', PostListView.as_view(model=PhotoPost, queryset=PhotoPost.objects.all(), template_name="blog/post_list.html")),
    url(r'^videos/?', PostListView.as_view(model=VideoPost, queryset=VideoPost.objects.all(), template_name="blog/post_list.html")),
    url(r'^quotes/?', PostListView.as_view(model=QuotePost, queryset=QuotePost.objects.all(), template_name="blog/post_list.html")),
    # Examples:
    # url(r'^$', 'topplr.views.home', name='home'),
    # url(r'^topplr/', include('topplr.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
