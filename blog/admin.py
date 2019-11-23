from django.contrib import admin

from blog.models import BlogPost
# Register your models here.

class BlogPostAdmin(admin.ModelAdmin):
    # pk:索引
    # 属性list_display表示要显示哪些属性
    list_display = ['pk', 'title', 'body', 'timestamp']


admin.site.register(BlogPost, BlogPostAdmin)