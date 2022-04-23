from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter, BaseRouter
from users.views import UserModelViewSet, UserListAPIView
from todo.views import ProjectView, TodoView
from rest_framework.authtoken import views
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from graphene_django.views import GraphQLView


schema_view = get_schema_view(
    openapi.Info(
        title="Library",
        default_version='0.1',
        description="документация",
        contact=openapi.Contact(email="admin@admin.local"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register('users', UserModelViewSet)
router.register('projects', ProjectView)
router.register('todo', TodoView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', views.obtain_auth_token),
    path('graphql/', GraphQLView.as_view(graphiql=True)),

    re_path(r'^api/(?P<version>\d.\d)/users/$', UserListAPIView.as_view()),
    path('api-path/', include('rest_framework.urls')),
    path('api/', include(router.urls)),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),
]
