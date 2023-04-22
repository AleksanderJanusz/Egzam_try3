"""
URL configuration for egzam project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main import views as main_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_views.main_views, name='main'),
    path('lecture_details/<int:lecture_id>/', main_views.lecture),
    path('set_username/<name>/', main_views.set_user),
    path('say_hello/<int:number>/', main_views.hello),
    path('say_hello/', main_views.hello_),
    path('create_cookie/<cookie_name>/<cookie_value>/<int:cookie_time>/', main_views.create_cookie),
    path('delete_cookie/<cookie_name>/', main_views.delete_cookie),
    path('add_student/', main_views.AddStudent.as_view()),



]
