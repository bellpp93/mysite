from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question

# Create your views here.
def index(request):
    """
        pybo 목록 출력
    """
    question_list = Question.objects.order_by('-create_date')  # -붙으면 내림차순 없으면 오름차순
    context = {'question_list': question_list}  # 딕셔너리의 {키 : 값}
    return render(request, 'pybo/question_list.html', context)  # 인자 값 3개

def detail(request, question_id):
    # question = Question.objects.get(id=question_id)  # get_object_or_404 추가 후 아래처럼 수정
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)