from django.conf.urls import url,include
from django.views.generic import ListView, DetailView
from posts.models import Posts
urlpatterns=[
    url(r'/news/All', ListView.as_view(queryset=Posts.objects.all().order_by("-date"),
    template_name="mainApp/includes/all.html") ),
]
