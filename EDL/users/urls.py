from django.conf.urls import url
from . import views
urlpatterns=[
url(r'^$', views.MainView.as_view()),
url(r'^login/$', views.login ),
url(r'^logout/$', views.logout),
url(r'^register/$', views.RegisterFormView.as_view())
]
