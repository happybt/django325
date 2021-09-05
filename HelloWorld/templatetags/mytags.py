# -*- coding: utf-8 -*-
#
# @Author：         TDZ
# @Time：           2021/9/4 21:43
# @Filename：       mytags.py
# @ProjectName：    django325 
# @IDE_Software：   PyCharm
#

from django import template

register = template.Library()

@register.filter
def myfilter(v1, v2):
    return v1 * v2

@register.simple_tag
def mytag(v1, v2, v3):
    return v1 * v2 * v3
