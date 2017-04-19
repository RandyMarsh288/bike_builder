"""bike_builder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from home import views as home_views
from accounts import views as accounts_views
from threads import views as forum_views
from merchandise import views as merchandise_views
from payments import views as payments_views
from django.views.static import serve
from .settings import MEDIA_ROOT



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_views.home_page, name='home'),

    # Accounts URLs
    url(r'^register/$', accounts_views.register, name='register'),
    url(r'^profile/$', accounts_views.profile, name='profile'),
    url(r'^login/$', accounts_views.login, name='login'),
    url(r'^logout/$', accounts_views.logout, name='logout'),

    # Forum URLs
    url(r'^forum/$', forum_views.forum, name='forum'),
    url(r'^threads/(?P<subject_id>\d+)/$', forum_views.threads, name='threads'),
    url(r'^new_thread/(?P<subject_id>\d+)/$', forum_views.new_thread, name='new_thread'),
    url(r'^thread/(?P<thread_id>\d+)/$', forum_views.thread, name='thread'),
    url(r'^post/new/(?P<thread_id>\d+)/$', forum_views.new_post, name='new_post'),
    # next line taken from lms but leads to issue in comment_details.html
    # url(r'^post/edit/(?P<thread_id>\d+)/$', forum_views.edit_post, name='edit_post'),
    # next line replaces line above using delete post code and seems to work
    url(r'^post/edit/(?P<thread_id>\d+)/(?P<post_id>\d+)/$', forum_views.edit_post, name='edit_post'),
    url(r'^post/delete/(?P<thread_id>\d+)/(?P<post_id>\d+)/$', forum_views.delete_post, name='delete_post'),

    # Poll URLs
    url(r'^thread/vote/(?P<thread_id>\d+)/(?P<subject_id>\d+)/$', forum_views.thread_vote, name='cast_vote'),

    # Merchandise URLs
    url(r'^merchandise/$', merchandise_views.all_products, name='merchandise'),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),

    # Payments URLs
    url(r'^create_order/(?P<product_id>\d+)/$', payments_views.create_order, name='create_order'),
    url(r'^place_order/(?P<product_id>\d+)/$', payments_views.place_order, name='place_order'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
        ]
