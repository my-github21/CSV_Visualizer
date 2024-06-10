from django.contrib import admin
from django.urls import path
from app1 import views
urlpatterns = [
    path('',views.upload,name='upload'),
    #  path('files/', views.file_list, name='file_list'),
    # path('files/<int:pk>/', views.file_detail, name='file_detail'),
]
