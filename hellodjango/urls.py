from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hellodjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include('mobile.urls')),
    url(r'^admin', include(admin.site.urls)),
)
print settings.STATIC_URL
urlpatterns += static(settings.MEDIA_URL, document_root=settings.STATIC_URL)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
