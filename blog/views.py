from django.shortcuts import render
from django.http import HttpResponse
from blog.models import BlogPost
from django.template import loader, Context
# Create your views here.

def archive(request) :
    posts = BlogPost.objects.all()
    t = loader.get_template(("archive.html"))
    #c = Context({'posts': posts})
    # 上下文必须是一个字段，不能是一个Context实例
    return HttpResponse(t.render({'posts': posts}))