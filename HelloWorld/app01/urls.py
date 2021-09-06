# -*- coding: utf-8 -*-


from django.urls import path
from . import views

urlpatterns = [
    path('add_book/', views.add_book),
    path('add_note/', views.add_note),
]
