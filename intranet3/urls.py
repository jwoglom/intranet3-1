from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'intranet.views.home', name='home'),
    # url(r'^intranet/', include('intranet.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns+= patterns('core.views',
    (r'^$', 'disp_homepage'),
    (r'^welcome/$', 'disp_welcome'),
    (r'^blanktemplate/$', 'blank_template'),
    (r'^loginnew/$', 'login_template'),
)
urlpatterns+= patterns('auth.views',
    (r'^login/$', 'disp_login'),
    (r'^auth/$', 'disp_auth'),
)
