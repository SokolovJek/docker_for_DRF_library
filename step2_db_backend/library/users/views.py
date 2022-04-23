from django.shortcuts import render
from .models import Users
from .serializers import AuthorsModelSerializers, AuthorsModelSerializersMore
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import mixins, generics



class UserModelViewSet(ModelViewSet):
    queryset = Users.objects.all()
    # serializer_class = AuthorsModelSerializers

    def get_serializer_class(self):
        if self.request.version == '0.2':
            return AuthorsModelSerializersMore
        return AuthorsModelSerializers


class UserListAPIView(generics.ListAPIView):
    queryset = Users.objects.all()
    # serializer_class = AuthorsModelSerializers

    def get_serializer_class(self):
        if self.request.version == '0.2':
            return AuthorsModelSerializersMore
        return AuthorsModelSerializers


# class AuthorModelViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, GenericViewSet):
#     queryset = Author.objects.all()
#     serializer_class = AuthorsModelSerializers

