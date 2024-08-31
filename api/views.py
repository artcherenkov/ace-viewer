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

    class Meta:
        model = File
        fields = ['filename', 'date_created', 'date_updated', 'size']


class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_class = FileFilter
    ordering_fields = ['filename', 'date_created', 'date_updated', 'size']
    ordering = ['-date_updated']
