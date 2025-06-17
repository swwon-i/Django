# Django 

## start
- django-admin startproject config . 
    - 현재 디렉터리에 config라는 이름으로 새로운 Django 프로젝트를 만듭니다. (.은 현재 디렉터리를 의미)
- django-admin startapp {app 이름} 또는 python manage.py startapp {app 이름}: 
    - {app 이름}으로 새로운 Django 앱(기능 단위)을 만듭니다. (뒤의 명령어가 더 흔히 사용됩니다.)
- python manage.py runserver: 
    -개발 중인 Django 웹 서버를 실행합니다.
---

### python manage.py startapp {app 이름}
> __init__.py
- 파이썬이 디렉토리를 인식할 수 있도록 하는 빈 파일

> admin.py
- 장고 관리자 페이지
- 여러 모델을 추가하면 쉽게 쉽게 관리 가능 

> app.py  
- 앱의 자동 설정을 담당
    - 앱 이름 설정
    - 이벤트 설정
    - 초기화 로직

> models.py
- 데이터베이스의 구조를 정의하는 역할
- 데이터를 어떻게 저장할 것인가

> test.py
- 테스트 코드 작성 파일

> urls.py
- 고전적인 방법
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
- include 방법
- board 관련 경로는 board에서 관리
    - board/urls.py
    ```
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('board/', include('board.urls')) # board의 urls 파일에서 board관련 경로를 관리
    ]
    ```

> views.py
- 웹 요청을 받으면 처리 및 응답 하는 뷰(view) 함수 저장하는  파일
---

### superuser
- python.exe .\manage.py migrate
    - 수수수슈퍼 계정 만들 준비
    - 데이터베이스 업데이트
- python manage.py createsuperuser
    - 수퍼수퍼 계정 만들기

