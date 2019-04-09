from django import template
from article.models import ArticlePost
from django.db.models import Count
from django.utils.safestring import mark_safe
import markdown

register = template.Library()


@register.simple_tag
def total_article():
    return ArticlePost.objects.count()


@register.simple_tag
def author_total_article(user):
    return user.article.count()


@register.inclusion_tag('article/list/latest_articles.html')
def latest_articles(n=5):
    latest_articles = ArticlePost.objects.order_by('-created')[:n]
    return {'latest_articles': latest_articles}


@register.simple_tag
def most_commented_articles(n=3):
    articles = ArticlePost.objects.annotate(total_comments=Count('comments')).order_by('-total_comments')[:n]
    return articles


@register.filter(name='markdown')
def markdown_filter(text):
    mk_text=text.replace('\n','  \n')
    return mark_safe(markdown.markdown(mk_text))
