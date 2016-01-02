import datetime
from django.db import models
from django.utils import timezone   
from django.utils.encoding import python_2_unicode_compatible
from tinymce.models import HTMLField
from django.template.defaultfilters import slugify

#... Need blog post
class Blog(models.Model):
    blog_title = "Bryan's Blog"

blog_title = "Bryan's Blog"
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = HTMLField()
    pub_date = models.DateTimeField('date published')
    author = models.CharField(max_length=200)
    slug = models.SlugField(('slug'), max_length=60, blank=True)
    def save(self, *args, **kwargs):
        if not self.id:
            #Only set the slug when the object is created.
            self.slug = slugify(self.title) #Or whatever you want the slug to use
        super(Post, self).save(*args, **kwargs)
    def __str__(self):
        return self.title
    '''
@python_2_unicode_compatible  # only if you need to support Python 2
class Question(models.Model):
    # ...
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

@python_2_unicode_compatible  # only if you need to support Python 2
class Choice(models.Model):
    # ...
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
        '''