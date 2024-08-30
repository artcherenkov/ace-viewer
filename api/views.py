from rest_framework import viewsets, filters
from .models import Note, Task, File
from .serializers import NoteSerializer, TaskSerializer, FileSerializer
import django_filters
from django_filters.rest_framework import DjangoFilterBackend


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class FileFilter(django_filters.FilterSet):
    filename = django_filters.CharFilter(lookup_expr='icontains')
    size_gte = django_filters.NumberFilter(field_name='size', lookup_expr='gte')
    size_lte = django_filters.NumberFilter(field_name='size', lookup_expr='lte')
    date_created = django_filters.DateTimeFilter(field_name='date_created', lookup_expr='date')
    date_created_gte = django_filters.DateTimeFilter(field_name='date_created', lookup_expr='gte')
    date_created_lte = django_filters.DateTimeFilter(field_name='date_created', lookup_expr='lte')
    date_updated_gte = django_filters.DateTimeFilter(field_name='date_updated', lookup_expr='gte')
    date_updated_lte = django_filters.DateTimeFilter(field_name='date_updated', lookup_expr='lte')

    class Meta:
        model = File
        fields = ['filename', 'date_created', 'date_updated', 'size']


class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_class = FileFilter
    ordering_fields = ['filename', 'date_created', 'date_updated', 'size']
