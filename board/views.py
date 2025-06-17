from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Question, Answer

def index(request):
    questions = Question.objects.order_by('-created_at')  # 질문을 생성 시간 기준으로 내림차순 정렬
    return render(request, 'board/index.html', {'questions': questions})

def detail(request, question_id):
    # question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, id=question_id)
            
    return render(request, 'board/detail.html', {'question' : question})

def create_answer(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    Answer(question=question, content=request.POST.get('content')).save()

    return redirect('board:question_detail', question_id=question.id)

def create_question(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        content = request.POST.get('content')
        question = Question(subject=subject, content=content)
        question.save()
        return redirect('board:question_list')
    return render(request, 'board/create_question.html')