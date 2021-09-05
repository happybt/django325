# -*- coding: utf-8 -*-
#
# @Author：         TDZ
# @Time：           2021/9/5 05:02
# @Filename：       search2.py
# @ProjectName：    django325 
# @IDE_Software：   PyCharm
#

from django.shortcuts import render
from django.views.decorators import csrf


# 接收POST请求数据
def search_post(request):
    ctx = {}
    if request.POST:
        ctx['rlt'] = request.POST['q']
    return render(request, 'post.html', ctx)
