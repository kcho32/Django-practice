from django.shortcuts import render, get_object_or_404
from .models import Question

# Create your views here.
#polls/ 요청시 
#latest_question_list에 Question의 모든데이터 select all
#teamplates - index.html select(latest_question_listwjsekf)

def index(request):
    #business method 호출 = question목록 가져오기
    #SELECT * FROM polls_question ORDER BY 
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    #일정 범위에 data 저장
    context = {'latest_question_list': latest_question_list}
    #template select
    return render(request, 'polls/index.html',context)


#polls/id/ 요청시 id에 해당하는 choice 항목 출력
#vote button 출력
def detail(request, question_id):
    #입력값 검증 : question_id
    #business method 호출 : question_id에 해당하는 Question
    #try:
    #   question = Question.objects.get(question_id)
    #except Question.DoesNotExist:
    #   raise Http404("Qeustion does not exist")
    #shortcut : get_object_or_404 이용
    question = get_object_or_404(Question, pk=question_id)
    #일정 범위에 data저장 - question
    #template select - polls/detail.html
    context = {'question': question}
    return render(request, "polls/detail.html",context)

##polls/id/vote 요청시 해당되는 id에 vote add한 후 결과 페이지로 redirecting한다
def vote(request, question_id):
    pass


#polls/id/results/ 요청시 id에 해당되는 vote결과 출력
def results(request, question_id):
    pass