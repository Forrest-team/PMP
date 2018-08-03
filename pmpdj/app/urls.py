"""pmp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path

from app import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('getImgCode/', views.get_img_code, name='getImgCode'),
    path(r'rs_house/?P<int:cid>/?P<int:sid>', views.rs_house, name='rs_house'),
    path(r'rs_house/', views.rs_house, name='rs_house'),
    path('mineInfo/', views.user_mine_info, name='mineInfo'),
]


