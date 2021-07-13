from django.http.response import HttpResponseRedirect
from .models import TableOfTodo, Todo
from django.shortcuts import render, get_object_or_404
from django.urls import reverse


# Create your views here.
def index(request):
    whatto_list = TableOfTodo.objects.all()
    context = {'whatto_list': whatto_list}
    return render(request, 'todos/index.html', context)


def show_all(request):
    todo_list = Todo.objects.all().order_by('todo_date')
    context = {'todo_list' : todo_list}
    return render(request, 'todos/show_all.html', context)


def add_1(request):
    whatto_list = get_object_or_404(TableOfTodo, pk = 2)
    context = {'whatto_list' : whatto_list}
    return render(request,'todos/add.html', context)


def add_2(request):
    added_todo = Todo(title = request.POST['title'], contents=request.POST['content'], todo_date=request.POST['due_date'])
    added_todo.save()
    return HttpResponseRedirect(reverse('todos:add_1'))


def delete(request):
    todo_list = Todo.objects.all().order_by('todo_date')
    context = {'todo_list' : todo_list}
    return render(request, 'todos/delete.html', context)


def delete_2(request):
    delete_todo = Todo.objects.get(pk=request.POST['data_delete'])
    delete_todo.delete()
    return HttpResponseRedirect(reverse('todos:delete'))


def modify(request):
    todo_list = Todo.objects.all().order_by('todo_date')
    context = {'todo_list' : todo_list}
    return render(request, 'todos/modify.html', context)


def modify_2(request):
    modify_todo = Todo.objects.get(pk=request.POST['data_modify'])
    context = {'modify_todo':modify_todo}
    return render(request, 'todos/modify_2.html', context)


def modify_3(request):
    modify_todo = Todo.objects.get(pk=request.POST['modify_id'])
    modify_todo.title = request.POST['title']
    modify_todo.contents=request.POST['content']
    modify_todo.todo_date=request.POST['due_date']
    modify_todo.save()
    return HttpResponseRedirect(reverse('todos:modify'))


def detail_view(request):
    todo_list = Todo.objects.all().order_by('todo_date')
    context = {'todo_list' : todo_list}
    return render(request, 'todos/detail_view.html', context)


def specific(request, todo_id):
    todo_list = get_object_or_404(Todo, pk = todo_id)
    context = {'todo_list' : todo_list}
    return render(request, 'todos/specific.html', context)




