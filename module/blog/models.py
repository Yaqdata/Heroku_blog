# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(u'标题', max_length=255)
    slug = models.CharField(u'铅字', max_length=255)
    description = models.CharField(u'描述', max_length=255)
    content = models.TextField()
    published = models.BooleanField()
    created = models.DateTimeField()

    class Meta:
        ordering = ['-created']

    def __unicode__(self):
        return u'%s' %self.title

    def get_absolute_url(self):
        print self.slug
        return '/%s/' %(self.slug)
        #return reverse('post', args=[self.slug])
