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
# Create your views here.

class MainView(TemplateView):
    template_name = 'mainApp/homepage.html'
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
    success_url = "/login/"
    template_name = "users/register.html"

    def form_valid(self,form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

def login(request):
    args = {}
    args.update(request)
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
    return 0;
def logout():
    auth.loggout(request)
    return redirect('/')


# class LoginFormView(FormView):
#    form_class = AuthenticationForm
#    template_name = "users/authentication.html"
#    def form_valid(self,form):
#    return super(LoginFormView,self).form_valid(form)
