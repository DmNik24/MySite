from django.contrib import admin
from django.conf.urls import url,include
from django.views.generic import ListView, DetailView
from posts.models import Articles
from . import views

app_name = 'posts'
urlpatterns = [
    url(r'^(?P<pk>\d+)/$',DetailView.as_view(model= Articles, template_name = "posts/post.html")),
    url(r'^edit_post/(?P<pk>\d+)/$', views.EditPost.as_view(), name='update-post'),

]
