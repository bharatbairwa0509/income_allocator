"""
URL configuration for IncomeAllocator project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import  path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('signup', views.handleSignUp , name ='handleSignUp'),
    path('login', views.handeLogin, name="handleLogin"),
    path('logout', views.handelLogout, name="handleLogout"),
    path('rent/' , views.rent , name = 'rant'),
    path('transport/' , views.transport , name='transport'),
    path('entertainment/' , views.entertainment , name='entertainment'),
    path('other/' , views.other , name='other'),
    path('distributeI' , views.distributeI , name='distributeI'),
    path('expense_pie_chart_view' , views.expense_pie_chart_view , name='expense_pie_chart_view'),
    
]
