from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField('Название', primary_key=True, max_length=50)
    rus_title = models.CharField('Название на русском', max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Image(models.Model):
    title = models.CharField('Название/Краткое описание изображения', max_length=50, blank=True)
    url = models.URLField('Ссылка на изображение', max_length=300)
    tag = models.ForeignKey(Tag, on_delete=models.PROTECT)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


class Event(models.Model):
    title = models.CharField('Название', max_length=100)
    text = models.TextField('Описание', max_length=300)
    place = models.CharField('Место', max_length=200)
    date = models.DateField('Дата')
    time = models.TimeField('Время')
    chat_link = models.URLField('Ссылка на чат', max_length=200, blank=True)
    price = models.PositiveIntegerField('Цена',default=0)
    tags = models.ManyToManyField(Tag, db_table='event_to_tag')
    image = models.ForeignKey(Image, on_delete=models.PROTECT)

    # По пользователю
    users = models.ManyToManyField(User, related_name='subscriptions', blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'