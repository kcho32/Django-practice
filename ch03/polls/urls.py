from django.urls import path
from polls import views

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),#polls/ url polls
    path('<int:question_id>/', views.detail, name='detail'), #polls/2 polls:detail
    path('<int:question_id>/results/',views.results, name='results'),
    path('<int:question_id>/vote/',views.vote, name='vote'),
]