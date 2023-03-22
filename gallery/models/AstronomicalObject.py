from django.db import models


class AstronomicalObject(models.Model):
    title = models.CharField('Título', max_length=500)
    description = models.TextField('Descrição')
    image = models.ImageField('Foto', upload_to='pictures/%Y/%m/%d', blank=True)
