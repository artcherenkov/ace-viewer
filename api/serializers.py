import locale

from django.utils.timezone import now
from rest_framework import serializers
from datetime import timedelta
from .models import Note, Task, File


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'due_date', 'created_at', 'updated_at']


class FileSerializer(serializers.ModelSerializer):
    size = serializers.SerializerMethodField()
    date_created = serializers.SerializerMethodField()
    date_updated = serializers.SerializerMethodField()

    class Meta:
        model = File
        fields = [
            'id',
            'filename',
            'date_created',
            'date_updated',
            'size'
        ]

    def get_size(self, obj):
        if obj.size >= 1024 * 1024:
            return f"{obj.size / (1024 * 1024):.2f} МБ"
        elif obj.size >= 1024:
            return f"{obj.size / 1024:.2f} КБ"
        else:
            return f"{obj.size} байт"

    def get_date_created(self, obj):
        return self.format_relative_date(obj.date_created)

    def get_date_updated(self, obj):
        return self.format_relative_date(obj.date_updated)

    def format_relative_date(self, date):
        current_time = now()
        difference = current_time - date

        # Установка русской локали
        locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')

        if difference < timedelta(hours=24):
            return f"Сегодня в {date.strftime('%H:%M')}"
        elif timedelta(hours=24) <= difference < timedelta(days=2):
            return f"Вчера в {date.strftime('%H:%M')}"
        else:
            return date.strftime('%d %B %Y')  # Формат "11 сен 2024"
