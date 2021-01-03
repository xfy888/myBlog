from django.contrib import admin
from .models import Articles
# Register your models here.

# 函数代表功能
def show_login_name(modeladmin,request,queryset):
    print(request.user.username)

class ArticlesAdmin(admin.ModelAdmin):
    actions=[show_login_name]
    # 希望显示的字段
    # fields=("title","author","content")
    # 除去某一字段
    # exclude=("img",)
    # 表头
    list_display=("title","author","img","abstract","visited","created_at","cmodidied_at")
    # 搜索
    search_fields=("title","abstract","content")
    # 筛选条件
    # list_filter=list_display
    list_filter=("title",)

show_login_name.short_description ="打印当前登录的用户"

admin.site.register(Articles,ArticlesAdmin)