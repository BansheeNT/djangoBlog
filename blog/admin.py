from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','category','intro')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('article','name','content')

admin.site.register(Category,CategoryAdmin)
admin.site.register(Tag,TagAdmin)
admin.site.register(Article,ArticleAdmin)
admin.site.register(Comment,CommentAdmin)
# admin.site.register(Category)
# admin.site.register(Tag)
# admin.site.register(Blog)
# admin.site.register(Comment)