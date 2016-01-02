from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render

from .models import Post, Blog


def index(request):
    latest_post_list = Post.objects.order_by('-pub_date')[:5]
    template = loader.get_template('main/index.html')
    context = {
        'latest_post_list': latest_post_list,
        'blog_title': Blog.blog_title,
    }
    return HttpResponse(template.render(context, request))

def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'main/detail.html', {'post': post, 'blog_title': Blog.blog_title,})