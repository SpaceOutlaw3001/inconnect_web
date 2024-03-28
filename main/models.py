from django.db import models


class Tag(models.Model):
    name = models.CharField('Название', primary_key=True, max_length=50)
    rus_title = models.CharField('Название на русском', max_length=50)

    def __str__(self):
        return self.name


class Image(models.Model):
    title = models.CharField('Название/Краткое описание изображения', max_length=50)
    url = models.URLField('Ссылка на изображение', max_length=300)
    tag = models.ForeignKey(Tag, on_delete=models.PROTECT)

    def __str__(self):
        return self.title


class Event(models.Model):
    title = models.CharField('Название', max_length=100)
    text = models.TextField('Описание', max_length=300)
    place = models.CharField('Место', max_length=200)
    date = models.DateField('Дата')
    time = models.TimeField('Время')
    chat_link = models.URLField('Ссылка на чат', max_length=200)
    tags = models.ManyToManyField(Tag, db_table='event_to_tag')
    image = models.OneToOneField(Image, on_delete=models.PROTECT)
    # потом добавим пользователя

    def __str__(self):
        return self.title