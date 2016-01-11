from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Image, Post, Blog
from .forms import ImageForm

def index(request):
    latest_post_list = Post.objects.order_by('-pub_date')[:5]
    template = loader.get_template('main/index.html')
    print Blog
    blog_title = Blog.objects.order_by('title')[:1]
    #blog_title = Blog.title
    context = {
        'latest_post_list': latest_post_list,
         'blog_title': blog_title,
    }
    return HttpResponse(template.render(context, request))

def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    blog_title = Blog.objects.order_by('title')[:1]
    return render(request, 'main/detail.html', {'post': post, 'blog_title': blog_title,})


def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Image(imagefile = request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('main.views.list'))
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'main/list.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )