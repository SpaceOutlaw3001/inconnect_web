#from django_filters import rest_framework as filters
import django_filters as filters
from .models import Event, Tag, User

# Фильтр для Тегов
class TagFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Tag
        fields = ['name']


# Фильтр для Событий
class EventFilter(filters.FilterSet):
    tags = filters.ModelMultipleChoiceFilter(#CharFiltersInFilter(
        field_name='tags__name',
        lookup_expr='in',
        queryset=Tag.objects.all(),
        method="get_tags"
    )
    users = filters.ModelMultipleChoiceFilter(
        queryset=User.objects.all(),
        method="get_users"
    )
    created_by = filters.ModelMultipleChoiceFilter(
        queryset=User.objects.all(),
        method="get_created_by"
    )
    def get_event(self,queryset,field_name,value):
        print("tags",value)
        if value:
            queryset = queryset.filter(event__id=value)
        return queryset

    def get_tags(self,queryset,field_name,value):
        if value:
            queryset = queryset.filter(tags__in=value)
        return queryset

    def get_users(self,queryset,field_name,value):
        if value:
            queryset = queryset.filter(users__in=value)
        return queryset

    def get_created_by(self,queryset,field_name,value):
        if value:
            queryset = queryset.filter(created_by__in=value)
        return queryset

    class Meta:
        model = Event
        fields = ['tags', 'users', 'created_by']
