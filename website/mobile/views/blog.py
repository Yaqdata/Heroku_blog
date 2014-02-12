# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from module.blog.models import Post, Page, Category
from django.db.models import Q

class BaseView(object):
    '''
    '''
    def get_context_data(self, *args, **kwargs):
        '''
        '''
        print args
        print kwargs
        context = super(BaseView, self).get_context_data(**kwargs)
        try:
            context['categories'] = Category.available_list()
            #context['pages'] = Page.objects.filter(status=0)
            #context['hot_posts'] = Post.get_hot_posts(9)
            #context['online_num'] = 9
        except Exception, e:
            print e
            pass
            #logger.exception(u'加载信息出错', e)
        return context

class IndexView(BaseView, ListView):
    '''
    '''
    query = None
    template_name = 'base.html'
    def get_context_data(self, **kwargs):
        print super(IndexView, self).get_context_data(**kwargs)
        return super(IndexView, self).get_context_data(**kwargs)

    def get_queryset(self):
        #self.query = self.request.GET.get('s', None)
        #if self.query:
        #    qset = (Q(title_icontains=self.query)|Q(content_icontains=self.query))
        #    posts = Post.objects.defer('content', 'content_html').filter(qset, status=0)
        #else:
        #    posts = Post.objects.defer('content', 'content_html').filter(status=0)

        return Post.get_hot_posts(9)
        

class CategoryView(BaseView, ListView):
    '''
    '''
    object = None
    template_name = 'blog/index.html'
#    queryset = Post.objects.filter(status=0)

    def get_queryset(self):
        alias = self.kwargs.get('alias')
        try:
            self.category = Category.objects.get(alias=alias)
            print 'self.category is %s' %type(self.category)
        except Category.DoesNotExist:
            return []

        return self.category.post_set.defer('content', 'content_html').filter(status=0)

    def get_context_data(self, **kwargs):
        if hasattr(self, 'category'):
            kwargs['href'] = self.category.alias
            kwargs['title'] = self.category.name + '|'

        return super(CategoryView, self).get_context_data(**kwargs)

#class TagsListView(IndexView):
#    '''
#    '''
#    def get_queryset(self):
#        tag = self.kwargs.get('tag')
#        posts = Post.objects.difer('content', 'content_html').filter()

class PostDetailView(BaseView, DetailView):
    '''
    '''
    object = None
    template_name = 'blog/post.html'
    queryset = Post.objects.filter(status=0)
    slug_field = 'alias'
    def get(self, request, *args, **kwargs):
        if 'HTTP_X_FORWARDED_FOR' in request.META:
            ip = request.META['HTTP_X_FORWARDED_FOR']
        else:
            ip = request.META['REMOTE_ADDR']
        alias = self.kwargs.get('slug')
        try:
            post = self.queryset.get(alias=alias)
        except Post.DoesNotExist:

            context = super(PostDetailView, self).get_context_data(**kwargs)
            return render(request, '404.html', context)
        post.view_times += 1
        post.save()
        return super(PostDetailView, self).get(request, *args, **kwargs)
    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        return context
