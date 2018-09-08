from django.conf.urls import url,include
from . import views
from django.views.generic import ListView, DetailView
from posts.models import Articles

urlpatterns=[
    #url(r'^$',views.index, name="index"),
    #url(r'^$', views.MainView.as_view(), name='index'),
    url(r'^$', ListView.as_view(queryset=Articles.objects.all().order_by("-date"),
    template_name="mainApp/homePage.html")),
    url(r'auth/$', views.login ),
    url(r'logout/$', views.logout),
    url(r'register/$', views.RegisterFormView.as_view()),
    url(r'profile/', ListView.as_view(queryset=Articles.objects.all().order_by("-date"),
    template_name="mainApp/profile.html")),
    url(r'add_post/', views.AddPost.as_view(), name='post_create')
]
