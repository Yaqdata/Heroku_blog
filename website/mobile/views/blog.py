# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from module.blog.models import Post, Page, Category
from django.db.models import Q

#logger = logging.getLogger(__name__)
def base(request):
    top_clicks = 'xxx'

def index(request):
    posts = Post.objects.filter(published=True)
    return render(request, 'blog/index.html', {'posts': posts})

def post(request, slug):
    print slug
    post = get_object_or_404(Post, slug=slug)
    print post.pk
    return render(request, 'blog/post.html', {'post': post})

class BaseView(object):
    '''
    '''
    def get_context_data(self, *args, **kwargs):
        '''
        '''
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
    template_name = 'blog/index.html'
    def get_context_data(self, **kwargs):
        a = super(IndexView, self).get_context_data(**kwargs)
        print a
        return super(IndexView, self).get_context_data(**kwargs)

    def get_queryset(self):
        self.query = self.request.GET.get('s', None)
        if self.query:
            qset = (Q(title_icontains=self.query)|Q(content_icontains=self.query))
            posts = Post.objects.defer('content', 'content_html').filter(qset, status=0)
        else:
            posts = Post.objects.defer('content', 'content_html').filter(status=0)
        print posts
        return posts
