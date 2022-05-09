import imp
from multiprocessing import context
from django.shortcuts import render
from articles.models import Article
# Create your views here.
def article_details_view(request, id=None):
    article_obj = None
    if(id != None):
        article_obj = Article.objects.get(id=id)
    context = {
        'object' : article_obj,
    }
    return render(request , 'articles/details.html', context=context)