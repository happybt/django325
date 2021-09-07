# -*- coding: utf-8 -*-


from django.urls import path
from . import views

urlpatterns = [
    path('add_book/', views.add_book),
    path('add_note/', views.add_note),
    path('add_note_aggregate/', views.add_aggregate),
    path('add_note_annotate/', views.add_annotate),
    path('add_FQ/', views.add_FQ),
    path('add_emp/', views.add_emp),
]
