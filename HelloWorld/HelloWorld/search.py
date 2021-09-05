# -*- coding: utf-8 -*-
#
# @Author：         TDZ
# @Time：           2021/9/5 04:50
# @Filename：       search.py
# @ProjectName：    django325 
# @IDE_Software：   PyCharm
#

from django.http import HttpResponse
from django.shortcuts import render

# 表单
def search_form(request):
    return render(request, 'search_form.html')

# 接收请求数据
def search(request):
    request.encoding = 'utf-8'
    if 'q' in request.GET and request.GET['q']:
        message = '你搜索的内容为： ' + request.GET['q']
    else:
        message = '你提交了空表单'
    return HttpResponse(message)
