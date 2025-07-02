from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('', views.HomePage, name='HomePage'),
    path('articles/', views.article_list, name='articlelist'),
    path('<int:article_id>/', views.article_detail, name='article_detail'),
    path('search/', views.article_search, name='article_search'),
    path('search/', views.search_articles, name='search_articles'),

    #path('articles/<int:pk>/', views.article_detail, name='article_detail')
path('ajax/search/', views.ajax_search_articles, name='ajax_search_articles')

]

