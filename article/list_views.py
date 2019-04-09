from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import ArticlePost, ArticleColumn, Comment
from .forms import CommentForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.db.models import Count


def article_titles(request, username=None):
    if username:
        user = User.objects.get(username=username)
        article_title = ArticlePost.objects.filter(author=user)
        try:
            userinfo = user.userinfo
        except:
            userinfo = None
    else:
        article_title = ArticlePost.objects.all()
    paginator = Paginator(article_title, 3)
    page = request.GET.get('page')
    try:
        current_page = paginator.page(page)
        articles = current_page.object_list
    except PageNotAnInteger:
        current_page = paginator.page(1)
        articles = current_page.object_list
    except EmptyPage:
        current_page = paginator(paginator.num_pages)
        articles = current_page.object_list
    if username:
        return render(request, 'article/list/author_articles.html', {'articles': articles,
                                                                     'page': current_page,
                                                                     'userinfo': userinfo,
                                                                     'user': user})
    return render(request, 'article/list/article_titles.html', {'articles': articles,
                                                                'page': current_page})


def article_detail(request, id, slug):
    article = get_object_or_404(ArticlePost, id=id, slug=slug)
    views = article.article_views
    article.article_views += 1  # 增加浏览次数
    # hot_articles=ArticlePost.objects.all().order_by('-article_views')[:3] #取最热前三名

    # 浏览次数大于0，取前3
    hot_articles = ArticlePost.objects.filter(article_views__gt=0).order_by('-article_views')[:3]
    try:
        article.save()
    except Exception as e:
        print(e)

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.article = article
            new_comment.save()
    else:
        comment_form = CommentForm()
        article_tags_ids = article.article_tag.values_list("id", flat=True)
        similar_articles = ArticlePost.objects.filter(article_tag__in=article_tags_ids).exclude(id=article.id)
        similar_articles = similar_articles.annotate(same_tags=Count("article_tag")).order_by("-same_tags", "-created")[:4]
    return render(request, 'article/list/list_article_detail.html', {'article': article,
                                                                     'views': views,
                                                                     'hot_articles': hot_articles,
                                                                     'comment_form':comment_form,
                                                                     'similar_articles':similar_articles})


# 点赞
@csrf_exempt
@require_POST
@login_required(login_url='/account')
def user_like(request):
    article_id = request.POST.get('id')
    action = request.POST.get('action')
    if article_id and action:
        try:
            article = ArticlePost.objects.get(id=article_id)
            if action == 'like':
                article.users_like.add(request.user)
                return HttpResponse('1')
            else:
                article.users_like.remove(request.user)
                return HttpResponse('2')
        except:
            return HttpResponse('no')
