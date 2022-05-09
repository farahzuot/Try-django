import imp
from multiprocessing import context
from django.shortcuts import render
from articles.models import Article
# Create your views here.

def article_search_view(request):
    query_dict = request.GET # this is a dictionary
    try:
        query = int(query_dict.get('q'))
    except:
        query = None
    article_obj = None
    if query:
        article_obj = Article.objects.get(id=query)
    context = {
        'object' : article_obj,
    }
    return render(request , 'articles/search.html' , context=context)


def article_details_view(request, id=None):
    article_obj = None
    if id:
        article_obj = Article.objects.get(id=id)
    context = {
        'object' : article_obj,
    }
    return render(request , 'articles/details.html', context=context)