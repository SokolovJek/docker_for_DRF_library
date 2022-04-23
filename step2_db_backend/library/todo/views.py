from .models import ProjectModel, TodoModel
from .serializers import ProjectModelSerializers, TodoModelSerializers, TodoModelSerializersPost, \
    ProjectModelSerializersPost
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import UpdateModelMixin, RetrieveModelMixin, ListModelMixin, DestroyModelMixin, \
    CreateModelMixin
from rest_framework.pagination import LimitOffsetPagination
from .filter import ProjectFilter, TodoFilter
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import BasePermission
from rest_framework.permissions import IsAuthenticated


class MyPaginator(LimitOffsetPagination):
    default_limit = 6


class MyPaginatorTodoView(LimitOffsetPagination):
    default_limit = 20


class StaffOnly(BasePermission):
    """Здесь правами будут наделены пользователи-сотрудники (is_staff)."""

    def has_permission(self, request, view):
        return request.user.is_staff


# class ProjectView(ModelViewSet):
#     permission_classes = [IsAuthenticated]
#     queryset = ProjectModel.objects.all()
#     serializer_class = ProjectModelSerializers
#     # pagination_class = MyPaginator
#     filterset_class = ProjectFilter
#


class ProjectView(UpdateModelMixin, CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, ListModelMixin,
                  GenericViewSet):
    permission_classes = [IsAuthenticated]
    queryset = ProjectModel.objects.all()
    serializer_class = ProjectModelSerializers
    # pagination_class = MyPaginator
    filterset_class = ProjectFilter

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return ProjectModelSerializers
        else:
            return ProjectModelSerializersPost

    def create(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class TodoView(UpdateModelMixin, CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, ListModelMixin,
               GenericViewSet):
    queryset = TodoModel.objects.all()

    # serializer_class = TodoModelSerializers
    # pagination_class = MyPaginatorTodoView
    # filterset_class = TodoFilter

    # def destroy(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     print(instance.is_active)
    #     instance.is_active = False
    #     print(instance.is_active)
    #     instance.save()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

    def get_serializer_class(self):
        """меняем сериализатор взависимости от типа запроса"""
        if self.request.method in ['GET']:
            return TodoModelSerializers
        else:
            return TodoModelSerializersPost
