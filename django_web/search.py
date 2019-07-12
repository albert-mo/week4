# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response, render


# 表单
def search_form(request):
    return render_to_response('search_form.html')


# 接收POST请求数据
def search_post(request):
    ctx ={}
    if request.POST:
        ctx['rlt'] = request.POST['q']
    return render(request, "post.html", ctx)


# 接收请求数据
def search(request):
    request.encoding = 'utf-8'
    if 'q' in request.GET:
        if request.GET['q'] != '':
            message = '你搜索的内容为: ' + request.GET['q']
        else:
            message = '输入为空'
    else:
        message = '无效链接'
    return HttpResponse(message)
