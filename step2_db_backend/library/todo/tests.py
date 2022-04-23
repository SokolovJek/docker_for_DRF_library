from django.test import TestCase
import json
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
from mixer.backend.django import mixer
from .models import TodoModel, ProjectModel
from users.models import Users
from users.views import UserModelViewSet
from .views import ProjectView, TodoView
from django.contrib.auth import get_user_model


# APIRequestFactory «подменяет» объект запроса, который мы потом передаём во view.
#                       Этот класс:
#                         ● возвращает объект запроса;
#                         ● не делает настоящий запрос;
#                         ● используется для изолированной проверки view;
#                         ● используется редко, обычно для нестандартных случаев.
# APIClient — класс для удобной отправки REST-запросов  и сразу получать ответ. Этот класс используется наиболее часто.
#                       Этот класс:
#                         ● отправляет запрос;
#                         ● обычно используется для большинства тестов.
# APISimpleTestCase применяется очень редко: в случаях, когда тест не связан с базой данных.
#                       Этоткласс:
#                         ● не использует базу данных;
#                         ● удобен для тестирования внутренних функций;
#                         ● быстро исполняется.
#                         ● APITestCase.
#


# ● модуль json нужен для чтения содержимого ответа от сервера;
# ● TestCase — базовый класс для создания Django-теста;
# ● status содержит константы для ответов сервера;
# ● APIRequestFactory — фабрика для создания запросов;
# ● force_authenticate — функция для авторизации пользователя;
# ● APIClient — клиент для удобной отправки REST-запросов;
# ● APISimpleTestCase — класс для создания простых test cases;
# ● APIITestCase — класс для создания test cases для REST API;
# ● Mixer — библиотека для генерации тестовых данных;
# ● User — модель пользователя;
# ● AuthorModelViewSet — view set для работы с моделью Author;
# ● TodoModel, ProjectModel, Author — модели.

# user_model = Users.objects.first()
# project_model = ProjectModel.objects.first()


class TestAuthorViewSet(TestCase):
    def setUp(self):
        self.user_data = {'first_name': 'Nic',
                          'last_name': 'Sokolov',
                          'birthday_year': 1991,
                          'email': 'jeksok@maail.ru',
                          'position': 'developer',
                          'username': 'braun',
                          'password': 'geekbrains'}
        self.super_user = get_user_model().objects.create_superuser('admin', 'admin@com.com', 'admin12345')
        self.user = Users.objects.create_user('jek', 'jek@com.com', 'geekbrains')
        self.project = ProjectModel.objects.create(project_name='ForYou',
                                                   link_git='https://github.com/',
                                                   descriptions='ла')
        self.project.users.add(self.user)

        # APIRequestFactory

    def test_get_list_author(self):
        factory = APIRequestFactory()
        request = factory.get('api/users/')
        view = UserModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_list_project(self):
        factory = APIRequestFactory()
        request = factory.get('api/projects/')
        view = ProjectView.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_list_project_authenticate_user(self):
        factory = APIRequestFactory()
        request = factory.get('api/projects/')
        force_authenticate(request, self.super_user)
        view = ProjectView.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_author(self):
        factory = APIRequestFactory()
        request = factory.post('api/authors/', self.user_data)
        view = UserModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_project(self):
        factory = APIRequestFactory()
        request = factory.post('api/project/', {'project_name': 'сайт для ВАС',
                                                'users': self.user,
                                                'link_git': 'git/mru.com',
                                                'descriptions': '........'})
        view = ProjectView.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_todo(self):
        factory = APIRequestFactory()
        request = factory.post('api/todo/', {'project': self.project,
                                             'todo_descriptions': 'сделать верстку и макет',
                                             'users': self.user})
        view = TodoView.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_admin(self):
        factory = APIRequestFactory()
        request = factory.post('api/users/', self.user_data)
        force_authenticate(request, self.super_user)
        view = UserModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # # APIClient
    def test_get_detail(self):
        client = APIClient()
        response = client.get(f'/api/users/{self.user.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_author(self):
        client = APIClient()
        response = client.put(f'/api/users/{self.user.id}/', self.user_data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_edit_author_and_authorize(self):
        client = APIClient()
        client.login(username='admin', password='admin12345')
        response = client.put(f'/api/users/{self.user.id}/', self.user_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        user = Users.objects.get(id=self.user.id)
        self.assertEqual(user.first_name, 'Nic')
        client.logout()

    # APISimpleTestCase

    def test_sqrt(self):
        import math
        self.assertEqual(math.sqrt(4), 2)

    # APITestCase
    def test_get_project_for_admin(self):
        self.client.login(username='admin', password='admin12345')
        response = self.client.get(f'/api/projects/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.client.logout()

    def test_edit_project_for_admin(self):
        self.client.login(username='admin', password='admin12345')
        response = self.client.patch(f'/api/projects/{self.project.id}/',
                                     json.dumps({'project_name': 'ForMe'}), content_type='application/json')
        project = ProjectModel.objects.get(id=self.project.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(project.project_name, 'ForMe')
