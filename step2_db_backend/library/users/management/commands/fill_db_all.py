from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from todo.models import TodoModel, ProjectModel
import random


class Command(BaseCommand):
    help = 'Create Users to test'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int)

    def handle(self, *args, **options):
        get_user_model().objects.all().delete()
        get_user_model().objects.create_superuser(username='django',
                                                  email='django@mail.ru',
                                                  password='geekshop',
                                                  first_name='jek',
                                                  last_name='sokolov'
                                                  )
        print(f'superuser created')

        count = options['count']
        for i in range(count):
            i += 1
            user = get_user_model().objects.create_user(username=f'name{i}',
                                                          email=f'user{i}@mail.ru',
                                                          password='geekshop',
                                                          first_name=f'Name{i}',
                                                          last_name=f'Sokolov{i}',
                                                          position='Backend-разработчик',
                                                          birthday_year=1990 + i
                                                          )
            print(f'user {user} created')

        TodoModel.objects.all().delete()
        ProjectModel.objects.all().delete()

        project = [
            {'project_name': 'TTT', 'link_git': 'https://github.com/TTT/TTT',
             'descriptions': 'Интернет магазин TTT'},
            {'project_name': 'ФНС', 'link_git': 'https://github.com/FNS/1',
             'descriptions': 'Приложение ФНС'},
        ]

        todo = [
            {'project': '', 'todo_descriptions': 'сделать верстку для сайта', 'users': ''},
            {'project': '', 'todo_descriptions': 'создать макет для сайта', 'users': ''},
            {'project': '', 'todo_descriptions': 'сделать API для приложения', 'users': ''},
            {'project': '', 'todo_descriptions': 'оптимизация проэкта', 'users': ''}
        ]

        for item in project:
            # item['users'] = get_user_model().objects.first()
            # a = ProjectModel.objects.create(**item)
            # a.objects.add(get_user_model().objects.first())
            a = ProjectModel(**item)
            a.save()
            a.users.set(get_user_model().objects.all())
            a.save()
        print('done, create set project model')

        for item in todo:
            item['project'] = ProjectModel.objects.first()
            item['users'] = get_user_model().objects.first()
            TodoModel.objects.create(**item)
        print('done, create set todo model')
        print('done!!! load all data for db. ')
