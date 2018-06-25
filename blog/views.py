from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,render_to_response

# Create your views here.
from blog.models import *
from blog.forms import CommentForm
from django.http import Http404
from django.core.paginator import Paginator ,PageNotAnInteger ,EmptyPage
import markdown

def get_articles(request,page):
    context = {}
    article_list= Article.objects.all().order_by('-createdTime')
    archive_list = Article.objects.distinct_date()
    category_list = Category.objects.all().order_by('-id')
    paginator = Paginator(article_list, 2)
    try:
        # 尝试获取请求的页数的信息
        articles = paginator.page(int(page))
    #请求页数错误
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(1)
    context['page_count'] = paginator.num_pages
    # for article in articles:
    #     article.content = markdown.markdown(article.content)
    context['articles'] = articles
    context['archive_list'] = archive_list
    context['category_list'] = category_list
    return render(request,'blog/article_list.html',context)

def get_details(request,article_id):
    try:
        article = Article.objects.get(id=article_id)
        # 将博客内容用markdown显示出来
        article.content = markdown.markdown(article.content,extensions=[
            'extra',
            'admonition',
            'headerid',
            'meta',
            'nl2br',
            'sane_lists',
            'smarty',
            'toc',
            'codehilite(linenums=True)',
            'wikilinks',
        ])
    except Article.DoesNotExist:
        raise Http404
    if request.method == 'GET':
        form = CommentForm()
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            cleaned_data['article'] = article
            Comment.objects.create(**cleaned_data)
    ctx = {
        'article':article,
        'comments':article.comment_set.all().order_by('-createdTime'),
        'form':form
    }
    return render(request,'blog/article_details.html',ctx)

def classify(request):
# 接收从url中传递的两个参数。
    context = {}
    categoryId = request.GET.get('category_id', None)
    page = request.GET.get('page', None)
    categoryName = request.GET.get('category_name', None)
    article_list = Article.objects.all().filter(category = int(categoryId)).order_by('-createdTime')
    # 分成 8 个一页。
    paginator = Paginator(article_list,8)
    try:
        # 尝试获取请求的页数的信息
        articles = paginator.page(int(page))
    #请求页数错误
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    context['categoryId'] = categoryId
    context['categoryName'] = categoryName
    context['page'] = page
    context['articles'] = articles
    return render(request,'blog/classify.html',context)

def tag(request):
# 接收从url中传递的两个参数。
    context = {}
    tagId = request.GET.get('tag_id', None)
    tagName = request.GET.get('tag_name', None)
    page = request.GET.get('page', None)
    article_list = Article.objects.all().filter(tags = int(tagId)).order_by('-createdTime')
    # 分成 8 个一页。
    paginator = Paginator(article_list,8)
    try:
        # 尝试获取请求的页数的信息
        articles = paginator.page(int(page))
    #请求页数错误
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    context['tagId'] = tagId
    context['tagName'] = tagName
    context['page'] = page
    context['articles'] = articles
    return render(request,'blog/tag.html',context)

def archive(request):
    context = {}
    year = request.GET.get('year', None)
    month = request.GET.get('month', None)   # 取出两个参数 year,month
    page = request.GET.get('page', None)
    article_list = Article.objects.filter(date__contains=year+'-'+month).order_by('-createdTime')
    # 根据参数year,month进行过滤， 记得字段名+__icontains 表大小写不敏感的包含匹配
    paginator = Paginator(article_list, 8)
    try:
        # 尝试获取请求的页数的信息
        articles = paginator.page(int(page))
    #请求页数错误
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    context['year'] = year
    context['month'] = month
    context['articles'] = articles
    return render(request, 'blog/archive.html', context)

def about(request):
    return render(request,'blog/about.html')