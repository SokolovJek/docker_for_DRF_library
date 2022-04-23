from django.contrib import admin
from todo.models import ProjectModel, TodoModel


admin.site.register(ProjectModel)
admin.site.register(TodoModel)
