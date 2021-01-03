from django.contrib import admin
from .models import Articles
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    # 表头
    list_display = ("title","author","abstract","visited")
    # 搜索

admin.site.register(Articles,ArticleAdmin)