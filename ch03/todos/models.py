from django.db import models

# Create your models here.

#맨 처음에 목차를 보여주어 어떤 작업을 할 것인지 선택하는 클래스
#선택지 number를 받을 예정
#선택지는 목록보기, 등록, 상세보기, 삭제, 수정
class TableOfTodo(models.Model):
    what_to_do = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.what_to_do


#선택지에 따른 결과값을 전송?
class Todo(models.Model):
    title = models.CharField(max_length=200)
    contents = models.CharField(max_length=200)
    todo_date = models.DateTimeField('Due dates')

    def __str__(self):
        return self.title
    