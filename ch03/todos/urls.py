from django.urls import path
from todos import views

app_name = 'todos'

urlpatterns = [
    path('', views.index, name='index'),#todos/ url polls
    path('1/', views.show_all, name='show_all'),
    path('2/', views.add_1, name='add_1'),
    path('2/add_2', views.add_2, name='add_2'),
    path('3/', views.detail_view, name='detail_view'),
    path('3/<int:todo_id>/', views.specific, name='specific'),
    path('4/', views.delete, name='delete'),
    path('4/delete_2/', views.delete_2, name='delete_2'),
    path('5/', views.modify, name='modify'),
    path('5/modify_2', views.modify_2, name='modify_2'),
    path('5/modify_3', views.modify_3, name='modify_3'),
]