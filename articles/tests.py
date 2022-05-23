from curses import qiflush
from django.test import TestCase
from .models import Article
from django.utils.text import slugify
# Create your tests here.
class ArticleTestCase(TestCase):
    def setUp(self):
        self.numbers_of_articles = 5
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