# -*- coding: utf-8 -*-

from django import forms
from django.core.exceptions import ValidationError
from . import models

"""
Django Form 组件用于对页面进行初始化，生成 HTML 标签，此外还可以对用户提交对数据进行校验（显示错误信息）。
报错信息显示顺序：
    1.先显示字段属性中的错误信息，然后再显示局部钩子的错误信息。
    2.若显示了字段属性的错误信息，就不会显示局部钩子的错误信息。
    3.若有全局钩子，则全局钩子是等所有的数据都校验完，才开始进行校验，并且全局钩子的错误信息一定会显示。

使用 Form 组件，需要先导入 forms：
from django import forms
"""


class EmpForm(forms.Form):
    """
    字段属性：

    label：输入框前面的文本信息。
    error_message：自定义显示的错误信息，属性值是字典，
        其中 required 为设置不能为空时显示的错误信息的 key。
    """
    name = forms.CharField(min_length=4, label='姓名', error_messages={'min_length': '你太短了', 'required': '该字段不能为空'})
    age = forms.IntegerField(label='年龄')
    salary = forms.DecimalField(label='工资')
