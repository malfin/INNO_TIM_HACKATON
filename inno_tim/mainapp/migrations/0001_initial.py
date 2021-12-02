# Generated by Django 3.2.9 on 2021-12-02 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Command',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('about', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Команда',
                'verbose_name_plural': 'Команды',
            },
        ),
        migrations.CreateModel(
            name='Startup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Наименование команды/организации')),
                ('product_readiness', models.CharField(choices=[('idea', 'Идея'), ('prototype', 'Прототип'), ('product', 'Продукт')], default='idea', max_length=32, verbose_name='Стадия готовности продукта')),
                ('product_description', models.TextField(max_length=500, verbose_name='Краткое описание продукта')),
                ('product_use_case', models.TextField(verbose_name='Кейсы использования продукта')),
                ('product_benefits', models.TextField(verbose_name='Польза продукта')),
                ('organization', models.CharField(choices=[('subway', 'Московский метрополитен'), ('mosgortrans', 'мосгорстранс'), ('sodd', 'ЦОДД'), ('transportation_organizer', 'Организатор перевозок'), ('mostransproekt', 'Мостранспроект'), ('ampp', 'АМПП')], default='subway', max_length=32, verbose_name='Организация Московского транспорта, интересная в первую очередь')),
                ('request_pilot_project', models.TextField(verbose_name='Запрос к акселератору и видение пилотного проекта')),
                ('certificate', models.CharField(choices=[('yes_or', 'да, требуется сертификация и у нас она есть'), ('yes_no', 'да, требуется сертификация, но  у нас ее нет'), ('no', 'нет, не требуется')], default='yes_or', max_length=10, verbose_name='Требуется ли сертификация продукта')),
                ('contact_full_name', models.CharField(max_length=128, verbose_name='ФИО контактного лица по заявке')),
                ('contact_position', models.CharField(max_length=128, verbose_name='Должность контактного лица')),
                ('phone', models.CharField(max_length=13, verbose_name='Контактный телефон')),
                ('email', models.EmailField(max_length=254, verbose_name='Контактная почта')),
                ('legal_entities', models.CharField(max_length=32, verbose_name='Наименование юридического лица')),
                ('inn', models.IntegerField(verbose_name='ИНН юридического лица')),
                ('people', models.CharField(max_length=32, verbose_name='Сколько человек в организации')),
                ('site', models.URLField(verbose_name='Сайт')),
                ('acselerator', models.TextField(verbose_name='Откуда узнали про акселератор')),
                ('presentation', models.URLField(verbose_name='Ссылка на презентацию')),
            ],
            options={
                'verbose_name': 'заявка',
                'verbose_name_plural': 'заявки',
            },
        ),
    ]
