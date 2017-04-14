# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404
from .models import Post
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.views.generic import ListView
from .forms import EmailPost

# Create your views here.


class PostListView(ListView):
    queryset = Post.objects.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post_list.html'

def post_list(request):
    object_list=Post.objects.all()
    paginator=Paginator(object_list,2)
    page=request.GET.get('page')
    try:
        posts=paginator.page(page)

    except PageNotAnInteger:
        posts=paginator.page(1)

    except EmptyPage:
        posts=paginator.page(paginator.num_pages)
    return render(request,'blog/post_list.html',{'page':page,'posts':posts})

def post_detail(request,year,month,day,post):
    post=get_object_or_404(Post,slug=post,
                                 publish__year=year,
                                 publish__month=month,
                                 publish__day=day)
    return render(request,'blog/post_detail.html',{'post':post})


def post_share(request,id):

    post=get_object_or_404(Post,id=id)

    if request.method=='POST':
        form=EmailPost('request.POST')
        if form.is_valid():
            cd=form.cleaned_data
            #send email
    else:
        form=EmailPost()
    render(request,'blog/post/share.html',{'post':post,'form':form})




