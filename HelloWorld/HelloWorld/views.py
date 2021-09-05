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
    '''
    常用的 request 属性。
    1、GET
    数据类型是 QueryDict，一个类似于字典的对象，包含 HTTP GET 的所有参数。
    有相同的键，就把所有的值放到对应的列表里。
    取值格式：对象.方法。
    get()：返回字符串，如果该键对应有多个值，取出该键的最后一个值。
    2、POST
    数据类型是 QueryDict，一个类似于字典的对象，包含 HTTP POST 的所有参数。
    常用于 form 表单，form 表单里的标签 name 属性对应参数的键，value 属性对应参数的值。
    取值格式： 对象.方法。
    get()：返回字符串，如果该键对应有多个值，取出该键的最后一个值。
    3、body
    数据类型是二进制字节流，是原生请求体里的参数内容，在 HTTP 中用于 POST，因为 GET 没有请求体。
    在 HTTP 中不常用，而在处理非 HTTP 形式的报文时非常有用，例如：二进制图片、XML、Json 等。
    4、path
    获取 URL 中的路径部分，数据类型是字符串。
    5、method
    获取当前请求的方式，数据类型是字符串，且结果为大写。

    响应对象：HttpResponse 对象
    响应对象主要有三种形式：HttpResponse()、render()、redirect()。
    HttpResponse(): 返回文本，参数为字符串，字符串中写文本内容。如果参数为字符串里含有 html 标签，也可以渲染。
    render(): 返回文本，
    第一个参数为 request，
    第二个参数为字符串（页面名称），
    第三个参数为字典（可选参数，向页面传递的参数：键为页面参数名，值为views参数名）。
    redirect()：重定向，跳转新页面。
    参数为字符串，字符串中填写页面路径。一般用于 form 表单提交后，跳转到新页面。
    render 和 redirect 是在 HttpResponse 的基础上进行了封装：
    render：底层返回的也是 HttpResponse 对象
    redirect：底层继承的是 HttpResponse 对象
    '''
    # name = request.GET.get('name')
    # name = request.POST.get('name')
    # return HttpResponse('姓名： {}'.format(name))

    # name = request.body

    # name = request.path

    # name = request.method

    name = '菜鸟教程666'
    views_dict = {'dname': '菜鸟教程dict', 'age': 18}
    # print(name)
    # return HttpResponse('菜鸟教程666')
    # return HttpResponse("<a href='https://www.runoob.com/'>菜鸟教程</a>")
    return render(request, 'hello.html', {'name', name})


def runoob(request):
    import datetime

    views_name = '菜鸟教程'
    views_list = ['菜鸟教程1','菜鸟教程2','菜鸟教程3','菜鸟教程4']
    views_list_empty = []
    views_dict = {'dname': '菜鸟教程dict', 'age': 18}
    views_default_name = 0
    views_number = 1024
    views_date_now = datetime.datetime.now()
    views_str = '菜鸟教程str'
    views_url =  "<a href='https://www.runoob.com/'>点击跳转</a>"

    return render(request, 'runoob.html',
                  {'views_name': views_name, 'views_list': views_list,
                   'views_dict': views_dict, 'views_defaultname': views_default_name,
                   'views_number': views_number, 'views_date_now': views_date_now,
                   'views_str': views_str, 'views_url': views_url,
                   'views_list_empty': views_list_empty,
                   })
