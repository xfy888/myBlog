from django.shortcuts import render
from .models import Articles

# Create your views here.

# FBV  function based view   基于函数的视图
def index(request):
    '''
        文章列表页
    '''
    # articles = Articles.objects.all().order_by('created_at')
    articles = Articles.objects.all()
    context = {
        "articles":articles
    }
    return render(request,'index.html',context)


def detail(request,pk):
    '''
        文章列表页
    '''
    article = Articles.objects.get(pk=pk)
    context = {
        'article':article
    }
    return render(request,'single_article.html',context)


def contact(request):
    '''
        联系我们
    '''
    return render(request,'contact.html')


def about(request):
    '''
        关于我
    '''
    return render(request,'about.html')


