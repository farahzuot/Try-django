from django.urls import path
from .views import (
    article_search_view,
    article_create_view,
    article_details_view,
)

app_name = 'articles'
urlpatterns = [
    path('', article_search_view, name='search'),
    path('create/', article_create_view, name='create'),
    path('<slug:slug>/', article_details_view, name='detail'),
]
