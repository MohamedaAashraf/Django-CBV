from django.urls import path
from . import views

urlpatterns = [
    path('',views.blog,name='blog'),
    path('<int:pk>',views.detail,name='detail'),
]