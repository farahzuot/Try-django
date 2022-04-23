from random import random
from django.http import HttpResponse;
from articles.models import Article;
from django.template.loader import render_to_string
import random

def home_view(request):
    rand = random.randint(1,3)
    # from database
    article_obj = Article.objects.get(id = rand)
    context = {
        'object' : article_obj,
    }
    HTML_STRING = render_to_string('home-view.html', context=context)
    return HttpResponse(HTML_STRING);
