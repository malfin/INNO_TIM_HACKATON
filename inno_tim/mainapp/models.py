from django.db import models


class Startup(models.Model):
    class Stage(models.TextChoices):
        IDEA = 'idea', 'Идея'
        PROTOTYPE = 'prototype', 'Прототип'
        PRODUCT = 'product', 'Продукт'

    class Organization(models.TextChoices):
        SUBWAY = 'subway', 'Московский метрополитен'
        MOSGOSTRANS = 'mosgortrans', 'мосгорстранс'
        SODD = 'sodd', 'ЦОДД'
        TRANSPORTATION_ORGANIZER = 'transportation_organizer', 'Организатор перевозок'
        MOSTRANSPROEKT = 'mostransproekt', 'Мостранспроект'
        AMPP = 'ampp', 'АМПП'

    class Certificate(models.TextChoices):
        YES = 'yes_or', 'да, требуется сертификация и у нас она есть'
        YES_NO = 'yes_no', 'да, требуется сертификация, но  у нас ее нет'
        NO = 'no', 'нет, не требуется'

    class People(models.TextChoices):
        LESS_20 = '20', 'Менее 20'
        FROM_20_100 = '20_100', 'от 20 до 100'
        FROM_100_500 = '100_500', 'от 100 до 500'
        MORE_500 = '500', 'более 500'

    name = models.CharField(verbose_name='Наименование команды/организации', max_length=256)
    product_readiness = models.CharField(verbose_name='Стадия готовности продукта', max_length=32,
                                         choices=Stage.choices, default=Stage.IDEA)
    product_description = models.TextField(verbose_name='Краткое описание продукта', max_length=500)
    product_use_case = models.TextField(verbose_name='Кейсы использования продукта')
    product_benefits = models.TextField(verbose_name='Польза продукта')
    organization = models.CharField(verbose_name='Организация Московского транспорта, интересная в первую очередь',
                                    max_length=32,
                                    choices=Organization.choices, default=Organization.SUBWAY)
    request_pilot_project = models.TextField(verbose_name='Запрос к акселератору и видение пилотного проекта')
    certificate = models.CharField(verbose_name='Требуется ли сертификация продукта', max_length=10,
                                   choices=Certificate.choices,
                                   default=Certificate.YES)
    contact_full_name = models.CharField(verbose_name='ФИО контактного лица по заявке', max_length=128)
    contact_position = models.CharField(verbose_name='Должность контактного лица', max_length=128)
    phone = models.CharField(verbose_name='Контактный телефон', max_length=13)
    email = models.EmailField(verbose_name='Контактная почта')
    legal_entities = models.CharField(verbose_name='Наименование юридического лица', max_length=32)
    inn = models.IntegerField(verbose_name='ИНН юридического лица')
    people = models.CharField(verbose_name='Сколько человек в организации', max_length=32)
    site = models.URLField(verbose_name='Сайт')
    acselerator = models.TextField(verbose_name='Откуда узнали про акселератор')
    presentation = models.URLField(verbose_name='Ссылка на презентацию')

    def __str__(self):
        return f'{self.name} | {self.product_readiness}'

    class Meta:
        verbose_name = 'заявка'
        verbose_name_plural = 'заявки'


class Command(models.Model):
    name = models.CharField(max_length=64)
    about = models.TextField(blank=True)
