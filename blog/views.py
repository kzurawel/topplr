from django.views.generic import DetailView, ListView
from blog.models import Tag, Post, NewsPost, VideoPost, PhotoPost, QuotePost

# Create your views here.

class PostListView(ListView):
    context_object_name = "posts"
    queryset = Post.objects.order_by('-pub_date').select_subclasses()

