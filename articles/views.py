import imp
from multiprocessing import context
from django.shortcuts import render,redirect
from django.http import Http404
from articles.models import Article
from django.contrib.auth.decorators import login_required
from articles.forms import ArticleForm
# Create your views here.


def article_search_view(request):
    query = request.GET.get('q')
    qs = Article.objects.search(query=query)
    context = {
        'object_list' : qs,
    }
    return render(request , 'articles/search.html' , context=context)

@login_required
def article_create_view(request, id=None):
    form = ArticleForm(request.POST or None)
    context = {'form': form}
    if form.is_valid():
        article_object = form.save()
        context['form'] = ArticleForm()
        return redirect(article_object.get_absolute_url())
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


def article_details_view(request, slug=None):
    article_obj = None
    if slug:
        try:
            article_obj = Article.objects.get(slug=slug)
        except Article.DoesNotExist:
            raise Http404
        except Article.MultipleObjectsReturned: # this will not happen for the way we build our server, but just extra info to return whatever when there is a repetition.
            article_obj = Article.objects.filter(slug=slug).first()
        except:
            raise Http404
    context = {
        'object' : article_obj,
    }
    return render(request , 'articles/details.html', context=context)