from django.urls import path
from . import views, list_views

app_name = 'article'
urlpatterns = [
    path('article_column', views.article_column, name='article_column'),
    path('rename_article_column', views.rename_column, name='rename_article_column'),
    path('del_article_column', views.del_column, name='del_article_column'),
    path('article_post', views.article_post, name='article_post'),
    path('article_list', views.article_list, name='article_list'),
    path('article_detail/<id>/<slug>', views.article_detail, name='article_detail'),
    path('del_article', views.del_article, name='del_article'),
    path('redit_article/<article_id>', views.redit_article, name='rdit_article'),
    path('list_article_titles', list_views.article_titles, name='list_article_titles'),
    path('list_article_detail/<id>/<slug>', list_views.article_detail, name='list_article_detail'),
    path('author_articles/<username>', list_views.article_titles, name='author_articles'),
    path('like_article', list_views.user_like, name='like_article'),
    path('article_tag', views.Article_tag, name='article_tag'),
]
