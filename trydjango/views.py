from random import random
from django.http import HttpResponse;
from articles.models import Article;
from django.template.loader import render_to_string
import random

def home_view(request):
    rand = random.randint(1,5)
    # from database
    # article_obj = Article.objects.get(id = rand)
    object_qs = Article.objects.all()
    context = {
        'object_qs' : object_qs,
        # 'object' : article_obj,
    }
    HTML_STRING = render_to_string('home-view.html', context=context)
    return HttpResponse(HTML_STRING);
