# -*- coding: utf-8 -*-
from django.contrib import admin
from blog.models import Post, Category, Page

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name', 'alias')
    list_displayer = ('name', 'rank', 'is_nav', 'status', 'created_at')

admin.site.register(Category, CategoryAdmin)

class PostAdmin(admin.ModelAdmin):
    #list_display = ['title', 'description']
    #list_filter = ['published', 'created']
    search_fields = ['title', 'alias']
    fields = ['content', 'author', 'summary', 'title', 'alias', 'tags', 'status', 'category', 'is_top', 'pub_time']
    
    ordering = ['pub_time']
    #date_hierarchy = 'created'
    save_on_top = True
    #prepopulated_fields = {'slug':('title',)}

admin.site.register(Post, PostAdmin)

class PageAdmin(admin.ModelAdmin):

    search_fields = ['title', 'alias']
    fields = ['content', 'author', 'title', 'alias', 'status']
    
admin.site.register(Page, PageAdmin)
