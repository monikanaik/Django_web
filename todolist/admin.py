from django.contrib import admin

# Register your models here.
from todolist.models import Category, TodoList


class TodoListAdmin(admin.ModelAdmin):
    list_display = ("title", "created", "due_date")


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


admin.site.register(Category)
admin.site.register(TodoList)
