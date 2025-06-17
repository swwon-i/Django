from django.db import models

# Create your models here.
class Question(models.Model):
    subject = models.CharField(max_length=200)  # 질문 제목 
    content = models.TextField()    # 질문 내용
    created_at = models.DateTimeField(auto_now_add=True) # 생성시간
    updated_at = models.DateTimeField(auto_now=True) # 수정 시간

    def __str__(self):
        return self.subject
    
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # 질문과의 관계 설정 -> 어떤 짐문에 대한 답변인지 내장
    content = models.TextField()    # 답변 내용
    created_at = models.DateTimeField(auto_now_add=True) # 생성시간
    updated_at = models.DateTimeField(auto_now=True) # 수정 시간

    def __str__(self):
        return f"Answer to : {self.question.subject}"