from django.db import models
from users.models import Users
from uuid import uuid4


class ProjectModel(models.Model):
    project_name = models.CharField(max_length=100)
    users = models.ManyToManyField(Users, related_name='all users for project')
    link_git = models.URLField()
    descriptions = models.TextField()
    date_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.project_name}'


class TodoModel(models.Model):
    STATUS_CHOICES = (
        ('ACTIVE', 'active'),
        ('DONE', 'done'),
    )

    project = models.ForeignKey(ProjectModel, on_delete=models.CASCADE, related_name='todo for project')
    todo_descriptions = models.TextField()
    users = models.ForeignKey(Users,
                              on_delete=models.CASCADE,
                              related_name='user_add_todo'
                              # models.SET_NULL,
                              # blank=True,
                              # null=True
                              )
    is_active = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.todo_descriptions
