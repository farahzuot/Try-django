from operator import mod
from django.conf import settings
from django.db import models
from django.urls import reverse
from .utils import slugify_instance_title
from django.db.models.signals import pre_save, post_save
from django.db.models import Q
# Create your models here.

User = settings.AUTH_USER_MODEL

class ArticleQuerySet(models.QuerySet):
    def search(self,query=None):
        if query == None:
            return self.none()
        lookups = Q(title__icontains=query) | Q(content__icontains=query)
        return self.filter(lookups)

class ArticleManager(models.Manager):
    def get_queryset(self):
        return ArticleQuerySet(self.model , using=self._db)

    def search(self,query=None):
        return self.get_queryset().search(query=query)


class Article(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True,blank=True , null=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    published = models.DateField(auto_now_add=False,auto_now=False , null=True, blank=True)

    objects = ArticleManager()

    def get_absolute_url(self):
        return reverse('articles:detail', kwargs={'slug':self.slug})
        
    def save(self, *args , **kwargs):
        # if self.slug == None:
        #     self.slug = slugify(self.title)
        super().save(*args, **kwargs)


def article_pre_save(sender, instance, *args, **kwargs):
    if instance.slug == None:
        slugify_instance_title(instance, save=False)
    
pre_save.connect(article_pre_save, sender=Article)



def article_post_save(sender, instance, created, *args, **kwargs):
    if created:
        slugify_instance_title(instance, save=True)

post_save.connect(article_post_save, sender=Article)