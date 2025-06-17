"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from board import views

# 해당 경로로 접속하면 뒤에 친구들이 실행
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('board/', views.index) # views.py 파일의 index 함수 의미
    path('board/', include('board.urls')) # board의 urls 파일에서 board관련 경로를 관리
]
