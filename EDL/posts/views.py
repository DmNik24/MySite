
from django.shortcuts import render
from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from . import models
from django.core.paginator import Paginator
from django.template.context_processors import csrf


def savepost(requestm):
    args = {}
    args.update(csrf(request))
    if request.POST:
        model = models.Articles
        title = request.POST.get('title')
        text = request.POST.get('text')
        model.title = title
        model.text = text
        if title is not None:
            model.save()
            return redirect('/profile')
        else:
            args['field_error']='Одно из полей пустое'
            return render_to_response('addPost.html', args)
    else:
        return render_to_response('addPost.html', args)
