import random
from datetime import datetime, timedelta
from django.utils.timezone import make_aware, now
from .models import File


def generate_mock_data(num_records=20):
    filenames = [
        "Смета'1000_2-1'Конструктивные решения_КР.gge",
        "Смета'1000_2-1'Архитектурные решения_АП.gge",
        "Смета'1000_2-1'Отопление и вентиляция_ОВ.gge",
        "Смета'1000_2-1'Водоснабжение и канализация_ВК.gge",
        "Смета'1000_2-1'Электроснабжение_ЭС.gge",
        "Смета'1000_2-1'Вентиляция и кондиционирование_ВК.gge",
        "Смета'1000_2-1'Энергоснабжение и освещение_ЭО.gge",
        "Смета'1000_2-1'Газоснабжение_ГС.gge",
        "Смета'1000_2-1'Слаботочные системы_СС.gge",
        "Смета'1000_2-1'Дренаж и ливневая канализация_ДЛК.gge",
        # Можно добавить свои названия для разнообразия
        "Смета'2000_3-1'Водоснабжение_ВС.gge",
        "Смета'3000_4-1'Электрооборудование_ЭО.gge",
    ]

    files = []

    start_date = make_aware(datetime.now() - timedelta(days=365 * 2))
    end_date = make_aware(datetime.now())

    for i in range(num_records):
        filename = random.choice(filenames)
        size = random.randint(100, 10240)  # Размер файла от 100 КБ до 10 МБ

        # Генерация случайных дат
        date_created = start_date + timedelta(seconds=random.randint(0, int((end_date - start_date).total_seconds())))
        date_updated = date_created + timedelta(
            seconds=random.randint(0, int((end_date - date_created).total_seconds())))

        file = File(
            filename=filename,
            date_created=date_created,
            date_updated=date_updated,
            size=size * 1024
        )
        files.append(file)

    # Сохранение всех сгенерированных объектов в базу
    File.objects.bulk_create(files)
