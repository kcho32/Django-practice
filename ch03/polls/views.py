from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Question, Choice
from django.urls import reverse

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
    #id 입력과 검증 후 Question을 가지고 온다.id 없으면 404에러
    #business logic 호출: question_id의 Question객체 select
    question = get_object_or_404(Question, pk=question_id)
    
    #request choice_id에 해당하는 vote조회 - 증가 - 업데이트(수정)
    #error : question, error_message 저장, detail.html template select
    #radio버튼은 1개만 선택 가능, checkbox는 복수 선택 가능
    try :
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        context = {'question' : question,'error_message' : "You didn't select a choice."}

        return render(request, 'polls/detail.html', context)#{
            #'question' : question,
            #'error_message' : "You didn't select a choice.",
        #}
        # context를 만들거나 주석처리 한 부분처럼 길게 써도 됨.
    else :
        #selected_choice의 vote값 증가 - 데이터베이스에 수정
        selected_choice.votes += 1
        selected_choice.save()
        #만약 데이터 수정이 이루어진다면 무조건 HttpResponseRedirect로 해줘야
        #이용자가 두번 클릭을 할 필요가 없어진다.
        return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))


#polls/id/results/ 요청시 id에 해당되는 vote결과 출력
def results(request, question_id):
    #id 입력과 검증 후 Question을 가지고 온다.id 없으면 404에러
    #business logic 호출: question_id의 Question객체 select
    question = get_object_or_404(Question, pk=question_id)
    #일정 범위에 데이타 저장, template select
    context = {'question' : question}
    return render(request, 'polls/results.html', context)
