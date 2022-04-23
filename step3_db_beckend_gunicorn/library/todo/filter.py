import django_filters


class ProjectFilter(django_filters.FilterSet):
    project_name = django_filters.CharFilter(label='введите имя проэкта',
                                             lookup_expr='contains')


class TodoFilter(django_filters.FilterSet):
    filter_date_gte = django_filters.NumberFilter(label='с какой даты показывать ToDo заметки',
                                                  field_name='date_create',
                                                  lookup_expr='day__gte')
    project__project_name = django_filters.CharFilter(label='введите имя проэкта',
                                                      lookup_expr='contains')
