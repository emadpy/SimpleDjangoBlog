from django.contrib import admin
from .models import Category, Post

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'published_jalali',
        'published_time',
        'updated_jalali',
        'updated_time',
        'slug',
    )
    list_filter = ('published_date', 'author')
    search_fields = ('title', 'content', 'author__username')