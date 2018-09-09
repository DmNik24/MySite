from django.shortcuts import render, render_to_response, redirect
from django.contrib import auth
from . import models
from django.core.paginator import Paginator
from django.template.context_processors import csrf
from django.views.generic import View, UpdateView
from posts.forms import PostForm
from posts.models import Articles
from posts import urls
from django.urls import reverse
from mainApp import urls

class EditPost(UpdateView):
    model = Articles
    form_class= PostForm
    template_name = "posts/edit_post.html"
    def get_success_url(self):
        return reverse('mainApp:lsit_posts')
