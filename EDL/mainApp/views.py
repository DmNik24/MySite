from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import logout
from users.models import Human
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib import auth
from django.shortcuts import render_to_response, redirect
from django.template.context_processors import csrf
from posts.forms import PostForm
from django.contrib.auth.hashers import make_password
from posts.models import Articles
from django.views.generic import View, ListView, UpdateView
from posts.models import *
from mainApp import urls
# Create your views here.

class MainView(TemplateView):
    template_name = 'mainApp/homePage.html'
    def get(self,request):
        if request.user.is_authenticated:
            humans = Human.objects.all()
            ctx={}
            ctx['humans'] = humans
            return render(request , self.template_name, ctx)

        else:
            return render(request , self.template_name, {})
class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "/auth/"
    template_name = "mainApp/register.html"

    def form_valid(self,form):
        forma = form.save(commit = False)
        form.password = make_password(forma.password)
        form.save()
        return super(RegisterFormView, self).form_valid(form)

class AddPost(View):
    def get(self, request):
        form= PostForm()
        return render(request,'addPost.html', context={'form':form})
    def post(self, request):
         bound_form = PostForm(request.POST)
         if bound_form.is_valid():
            new_post = bound_form.save(commit = False)
            new_post.user= request.user
            new_post.save()
            return redirect('/')
         return render(request, 'addPost.html', context={'form':bound_form})

def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username',)
        password = request.POST.get('password',)
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            args['login_error']='Пользователь не найден'
            return render_to_response('login.html', args)
    else:
        return render_to_response('login.html', args)

def logout(request):
    auth.logout(request)
    return redirect('/')
