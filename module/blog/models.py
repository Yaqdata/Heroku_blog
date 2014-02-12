# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
import datetime

STATUS = {
    0: u'正常',
    1: u'草稿',
    2: u'删除',
}
# Create your models here.
class Category(models.Model):
    '''
    类别
    '''
    name = models.CharField(u'名称', max_length=40)
    alias = models.CharField(u'英文名称', max_length=40, db_index=True)
    is_nov = models.BooleanField(u'是否显示', default=False)
    parent = models.ForeignKey('self', default=None, blank=True, null=True)
    desc = models.CharField(u'描述', max_length=100, blank=True)
    rank = models.IntegerField(u'排序',default=0)
    status = models.IntegerField(u'状态', default=0, choices=STATUS.items(), db_index=True)
    created_at = models.DateTimeField(u'创建时间', auto_now_add=True)
    updated_at = models.DateTimeField(u'更新时间', auto_now=True)

    def __unicode__(self):
        if self.parent:                                                                                                  
            return u'Category:%s:%s' % (self.parent, self.name)
        else:
            return u'Category:%s' % (self.name)

    class Meta:
        ordering = ['rank', '-created_at']
        verbose_name_plural = verbose_name = u"分类"

    @classmethod
    def available_list(cls):
        '''
        显示内容
        '''
        return cls.objects.filter(status=0)

class Page(models.Model):
    '''
    页面头
    '''
    author = models.ForeignKey(User)
    title = models.CharField(u'标题', max_length=100)
    alias = models.CharField(u'英文标题', max_length=100, blank=True, null=True)
    content = models.TextField(u'正文')
    content_html = models.TextField(u'正文')
    is_html = models.BooleanField(u'html代码', default=False)
    link = models.CharField(u'链接', max_length=200, blank=True, null=True)
    rank = models.IntegerField(u'排序', default=1)
    status = models.IntegerField(u'状态', default=0, choices=STATUS.items(), db_index=True)
    created_at = models.DateTimeField(u'创建时间', auto_now_add=True)
    updated_at = models.DateTimeField(u'更新时间', auto_now=True)
    
    def __unicode__(self):
        return u'%s' %title

    class Meta:
        ordering = ['rank', '-created_at']
        verbose_name_plural = verbose_name = u'页面'

class Post(models.Model):
    '''
    页面正文
    '''
    author = models.ForeignKey(User)
    category = models.ForeignKey(Category, db_index=True)

    title = models.CharField(u'标题', max_length=100, db_index=True)
    alias = models.CharField(u'英文标题', max_length=100, blank=True, null=True)
    is_top = models.BooleanField(u'置顶',default=False)
     
    summary = models.TextField(u'摘要')
    content = models.TextField(u'文章正文rst格式')
    
    content_html = models.TextField(u'文章正文html')
    view_times = models.IntegerField(u'查看次数', default=1)
    
    tags = models.CharField(u'标签', max_length=100, null=True, blank=True, help_text=u'用英文逗号分割', db_index=True)
    status = models.IntegerField(u'状态', default=0, choices=STATUS.items(), db_index=True)
    
    pub_time = models.DateTimeField(u'发布时间', default=datetime.datetime.now())
    
    created_at = models.DateTimeField(u'创建时间', auto_now_add=True, editable=True)
    updated_at = models.DateTimeField(u'更新时间', auto_now=True) 

    class Meta:
        ordering = ['-created_at']

    def __unicode__(self):
        return u'%s' %self.title

    def tag_list(self):
        '''
        标签
        '''
        return [tag.strip() for tag in self.tags.split(',')]

    @classmethod
    def get_recently_posts(cls, num):
        '''
        当前页的数量
        '''
        return cls.objects.values('title', 'alias').filter(status=0)[:num]
        #return cls.objects.values('title', 'alias').filter(status=0).order_by('-created_at')[:num]

    @classmethod
    def get_hot_posts(cls, num):
        '''
        点击率高
        '''
        return cls.objects.values('title', 'alias', 'summary').filter(status=0)[:num]
        #return cls.objects.values('title', 'alias').filter(status=0).order_by('-created_at')[:num]


    def get_related_posts(self):
        '''
        相关
        '''
        related_posts = None
        try:
            related_posts = Post.objects.values('title', 'alias').filter(tags__icontains=self.tags_list()[0]).\
                    exclude(id=self.pk)[:10]
        except IndexError:
            pass

        if not related_posts:
            related_posts = Post.objects.values('title', 'alias').filter(category=self.categoty).exclude(id=self.pk)[:10]

        return related_posts
