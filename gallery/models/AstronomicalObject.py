from django.db import models


class AstronomicalObject(models.Model):
    categories = (
        ('Galáxia', 'Galáxia'),
        ('Aglomerado', 'Aglomerado'),
        ('Estrela', 'Estrela'),
        ('Nebulosa', 'Nebulosa'),
        ('Planeta', 'Planeta'),
        ('Outros','Outros'),
    )

    title = models.CharField('Título', max_length=500)
    description = models.TextField('Descrição')
    image = models.ImageField('Foto', upload_to='pictures/%Y/%m/%d', blank=True)
    category = models.CharField('Categoria', choices=categories, max_length=20, default='Outros')
    published = models.BooleanField('Publicado', default=False)
