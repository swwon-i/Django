from django.urls import path
from . import views

# 네임스페이스
## board:question_list

app_name = 'board'

urlpatterns = [
    path('', views.index, name='question_list'),  
    path('<int:question_id>/', views.detail, name='question_detail'),
    path('ask/create/<int:question_id>', views.create_answer, name='create_answer' ),
    path('question/create', views.create_question, name='create_question' )
    
]