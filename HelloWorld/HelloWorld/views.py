# -*- coding: utf-8 -*-
#
# @Author：         TDZ
# @Time：           2021/9/1 16:07
# @Filename：       views.py.py
# @ProjectName：    django325 
# @IDE_Software：   PyCharm
#

from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return HttpResponse('hello world!')


def runoob(request):
    # context = {}
    # context['helo'] = 'heloworld'
    views_name = '菜鸟教程'
    return render(request, 'runoob.html', {'name': views_name})
