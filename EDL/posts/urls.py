from django.contrib import admin
from django.conf.urls import url,include
from django.views.generic import ListView, DetailView
from posts.models import Articles
from . import views
from mainApp.views import EditPost

urlpatterns = [
    url(r'(?P<pk>\d+)/$',DetailView.as_view(model= Articles, template_name = "posts/post.html")),
    url(r'edit_post/(?P<pk>\d+)/$', EditPost.as_view(), name='post_update_url'),
    url(r'edit_post/save/$', views.savepost),
]
