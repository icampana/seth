from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'seth.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'seth.views.home', name='home'),
#    url(r'^register/', 'seth.views.register', name='register' ),
    (r'^accounts/', include('registration.backends.default.urls')),


)
