from django.contrib import admin
from .models import TableOfTodo, Todo
# Register your models here.

admin.site.register(TableOfTodo)
admin.site.register(Todo)