from curses import qiflush
from django.test import TestCase
from .models import Article
from django.utils.text import slugify
from .utils import slugify_instance_title

# Create your tests here.
class ArticleTestCase(TestCase):
    def setUp(self):
        self.numbers_of_articles = 500
        for i in range(0, self.numbers_of_articles):
            Article.objects.create(title='Hello world!', content='this is the content field.')
    
    def test_queryset_exists(self):
        qs = Article.objects.all()
        self.assertTrue(qs.exists())
    
    def test_queryset_count(self):
        qs = Article.objects.all()
        self.assertEqual(qs.count(), self.numbers_of_articles)

    def test_hello_world_slug(self):
        obj = Article.objects.all().order_by('id').first()
        title = obj.title
        slug = obj.slug
        slugifiedTitle = slugify(title)
        self.assertEqual(slug, slugifiedTitle)

    def test_hello_world_unique_slug(self):
        qs = Article.objects.exclude(slug__iexact='hello-world')
        for obj in qs:
            title = obj.title
            slug = obj.slug
            slugifiedTitle = slugify(title)
            self.assertNotEqual(slug, slugifiedTitle)

    def test_slugify_instance_title(self):
        instance = Article.objects.all().last()
        newSlug = []
        for i in range(0,25):
            instance = slugify_instance_title(instance, save=False)
            newSlug.append(instance.slug)
        uniqueSlug = list(set(newSlug))
        self.assertEqual(len(newSlug),len(uniqueSlug))

    def test_slugify_instance_redux(self):
        slug_list = Article.objects.all().values_list('slug', flat=True)
        uniqueSlug = list(set(slug_list))
        self.assertEqual(len(slug_list),len(uniqueSlug))

    # def test_user_added_slug_unique(self):

    def test_search_article_manager(self):
        qs = Article.objects.search(query='hello world')
        self.assertEqual(qs.count(), self.numbers_of_articles)
        qs = Article.objects.search(query='hello')
        self.assertEqual(qs.count(), self.numbers_of_articles)
        qs = Article.objects.search(query='content field')
        self.assertEqual(qs.count(), self.numbers_of_articles)