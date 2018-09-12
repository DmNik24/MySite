from django.conf.urls import url,include
from . import views
from django.views.generic import ListView, DetailView
from posts.models import Articles

app_name = 'mainApp'
urlpatterns=[
    #url(r'^$',views.index, name="index"),
    #url(r'^$', views.MainView.as_view(), name='index'),
    url(r'^$', ListView.as_view(queryset=Articles.objects.all().order_by("-date"),
    template_name="mainApp/homePage.html"), name='lsit_posts'),
    url(r'auth/$', views.login ),
    url(r'logout/$', views.logout),
    url(r'register/$', views.RegisterFormView.as_view()),
    #url(r'profile/(?P<pk>\d+)/$', ListView.as_view(queryset=Articles.objects.all().order_by("-date"),
    #template_name="mainApp/profile.html")),
    url(r'add_post/', views.AddPost.as_view(), name='post_create'),
    url(r'profile/(?P<pk>\d+)/$', views.ViewProfile.as_view(), name='profile')
]
