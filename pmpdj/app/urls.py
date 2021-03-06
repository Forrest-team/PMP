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
from django.urls import path, re_path

from app import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('getImgCode/', views.get_img_code, name='getImgCode'),
    path('mineInfo/', views.user_mine_info, name='mineInfo'),
    path('complain/', views.complain, name='complain'),
    path('livingPay/', views.living_pay, name='livingPay'),
    path('updateInfo/', views.update_info, name='updateInfo'),
    path('getUserNo/', views.get_user_no, name='getUserNo'),
    path(r'rs_house/?P<int:cid>/?P<int:sid>', views.rs_house, name='rs_house'),
    path(r'rs_house/', views.rs_house, name='rs_house'),
    path('mineInfo/', views.user_mine_info, name='mineInfo'),
    re_path(r'rs_house/$', views.rs_house, name='rs_house'),
    path(r'rs_house/<int:cid>/<int:sid>/', views.rs_house_info, name='rs_house_info'),
    path('newhouse/', views.newhouse, name='newhouse')

]


