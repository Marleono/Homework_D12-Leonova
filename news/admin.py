from django.contrib import admin
from .models import Category, Post, PostCategory

# Register your models here.
class PostCategoryInline(admin.TabularInline):
    model = PostCategory
    extra = 1

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = (PostCategoryInline,)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = (PostCategoryInline,)
