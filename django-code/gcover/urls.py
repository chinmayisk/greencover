from django.conf.urls import patterns, include, url
from tastypie.api import Api
from greencover.api.resources import *

from django.contrib import admin
admin.autodiscover()

v1_api = Api(api_name = 'v1')
v1_api.register(UserModel())
v1_api.register(TreeModel())
v1_api.register(AchievementModel())

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'greencover.views.index', name='home'),
    url(r'^(\d+)/$', 'greencover.views.treeinfo', name='treeinfo'),
    url(r'^api/', include(v1_api.urls)),
    # url(r'^gcover/', include('gcover.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
