# coding:utf8
from django.contrib import admin



from blog.views import *
from django.conf.urls import url,include


urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$',get_articles,{'page': 1}),
    url(r'^(\d+)$',get_articles),
    url(r'^detail/(\d+)/$',get_details ,name='article_get_detail'),
    #分类
    # url(r'^classify/(\d+)/(\d+)/$',classify),
    url(r'^classify/$',classify,name='classify'),
    #标签
    url(r'^tag/$',tag,name='tag'),
    #按年月归档
    url(r'^archive/$', archive, name='archive' ),
    url(r'^about$', about, name='about' ),
]