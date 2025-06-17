# Django 


## start
- django-admin startproject config . 
    - 현재 디렉터리에 config라는 이름으로 새로운 Django 프로젝트를 만듭니다. (.은 현재 디렉터리를 의미)
- django-admin startapp {app 이름} 또는 python manage.py startapp {app 이름}: 
    - {app 이름}으로 새로운 Django 앱(기능 단위)을 만듭니다. (뒤의 명령어가 더 흔히 사용됩니다.)
- python manage.py runserver: 
    -개발 중인 Django 웹 서버를 실행합니다.

### urls
- config/urls.py
    - 이 파일 안에는 접속할 경로를 만들수 있음
    ```
    # path('A', B)
    ## A 경로로 접속 -> B 실행
    urlpatterns = [
    path('admin/', admin.site.urls),
    path('board/', views.index) # views.pt 파일의 index 함수 의미
    ]
    ```
###
