from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.login,  name='login'),
    path('addTodo', views.addTodo, name='addTodo'),
    path('addBlog', views.addBlog, name='addBlog'),
    path('submitBlog', views.submitBlog,  name='submitBlog'),
    path('displayBlog/<bl_id>', views.displayBlog,  name='displayBlog'),
    path('displaySignup', views.displaySignup,  name='displaySignup'),
    path('loginSuccess', views.loginSuccess,  name='loginSuccess'),
    
]
