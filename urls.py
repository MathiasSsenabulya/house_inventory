from django.conf.urls import patterns, include, url
from django.contrib import admin
##from house_inventory import views
from house_inventory.views import *
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'house_inventory.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^hello/$', hello),
    url(r'^showheaders/$', display_meta),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^item/add/$', item_add),
    url(r'^item/thanks/$', item_thanks)

)


##from mysite.views import hello, current_datetime, hours_ahead, display_meta
##admin.autodiscover()
##from books import views #figure out why this doesn't work as mysite.books
##
##urlpatterns = patterns('',
##    # Examples:
##    # url(r'^$', 'mysite.views.home', name='home'),
##    # url(r'^blog/', include('blog.urls')),
##
##    url(r'^admin/', include(admin.site.urls)),
##    url(r'^time/$', current_datetime),
##    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
##    url(r'^search/$', views.search),
##    url(r'^contact/$', views.contact),
##    url(r'^contact/thanks/$', views.contact_thanks),
##)
