from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
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
        count = options['count']
        for i in range(count):
            i += 1
            author = get_user_model().objects.create_user(username=f'name{i}',
                                                          email=f'user{i}@mail.ru',
                                                          password='geekshop',
                                                          first_name=f'Name{i}',
                                                          last_name=f'Sokolov{i}',
                                                          position='Backend-разработчик',
                                                          birthday_year=1990 + i
                                                          )
            print(f'author {author} created')
        print('done')

# # создаем группы
#         # младшие сотрудники
#         little_staff = Group.objects.create(name='Младшие сотрудники')
#         # права этой группы только книги, остальное просмотр
#
#         little_staff.permissions.add(add_book)
#         little_staff.permissions.add(change_book)
#         little_staff.permissions.add(delete_book)
#         # # старшие сотрудники
#
#         big_staff = Group.objects.create(name='Старшие сотрудники')
#         # права этой группы книги и авторы, остальное просмотр
#         big_staff.permissions.add(add_book)
#         big_staff.permissions.add(change_book)
#         big_staff.permissions.add(delete_book)
#
#         big_staff.permissions.add(add_author)
#         big_staff.permissions.add(change_author)
#         big_staff.permissions.add(delete_author)
#
#         # Остальные могу только смотреть
#
#         # Создаем пользователей и добавляем в группы
#         little = User.objects.create_user('little', 'little@little.com', 'geekbrains')
#         little.groups.add(little_staff)
#         little.save()
#
#         big = User.objects.create_user('big', 'big@big.com', 'geekbrains')
#         big.groups.add(big_staff)
#         big.save()
#
#         print('done')