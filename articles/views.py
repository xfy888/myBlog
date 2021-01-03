from django.shortcuts import render

# Create your views here.

def index(request):
    '''
        文章列表页
    '''
    return render(request,'index.html')


def detail(request):
    '''
        文章列表页
    '''
    return render(request,'single_article.html')


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


