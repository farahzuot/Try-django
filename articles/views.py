import imp
from multiprocessing import context
from django.shortcuts import render
from articles.models import Article
from django.contrib.auth.decorators import login_required
from articles.forms import ArticleForm
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

@login_required
def article_create_view(request, id=None):
    form = ArticleForm(request.POST or None)
    context = {'form': form}
    if form.is_valid():
        article_object = form.save()
        context['form'] = ArticleForm()
    return render(request , 'articles/create.html', context=context)


# old version_
# def article_create_view(request, id=None):
#     form = ArticleForm()
#     context = {'form': form}
#     if request.method == 'POST':
#         form = ArticleForm(request.POST)
#         context['form'] = form
#         if form.is_valid():
#             title = form.cleaned_data.get('title')
#             content = form.cleaned_data.get('content')
#             article_obj = Article.objects.create(title= title, content= content)
#             context = {
#                 'object': article_obj,
#                 'created': True,
#                 }

#     return render(request , 'articles/create.html', context=context)


def article_details_view(request, id=None):
    article_obj = None
    if id:
        article_obj = Article.objects.get(id=id)
    context = {
        'object' : article_obj,
    }
    return render(request , 'articles/details.html', context=context)