from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def home_page(request):
    latest_posts = Post.objects.all().order_by('-date')
    return render(request, "blog_site/templates/blog_site/index.html", {
        'posts': latest_posts
    })

def posts(request):
    all_posts = Post.objects.all().order_by('-date')
    return render(request, "blog_site/templates/blog_site/all_posts.html", {
        "all_posts": all_posts
    })

def posts_detail(request, slug):
    identified_post = get_object_or_404(Post, slug=slug)
    return render(request, "blog_site/templates/blog_site/posts_detail.html", {
        "post": identified_post,
        "post_tags": identified_post.tags.all(),
    })