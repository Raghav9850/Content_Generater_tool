# generator/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.input_form_view, name='input_form'),
    path('content/', views.content_display_view, name='content_display'),
    path('download/pdf/', views.download_pdf_view, name='download_pdf'),
    path('download/txt/', views.download_txt_view, name='download_txt'),
]
