from django.db import models
from django.contrib.auth.models import User


class Astrophotography(models.Model):
    categories = (
        ('Galáxia', 'Galáxia'),
        ('Aglomerado', 'Aglomerado'),
        ('Estrela', 'Estrela'),
        ('Nebulosa', 'Nebulosa'),
        ('Planeta', 'Planeta'),
    )

    title = models.CharField('Título', max_length=500)
    image_source = models.CharField('Fonte', max_length=50, default='')
    date_image = models.DateField('Data da Imagem', default='2000-01-01')
    description = models.TextField('Descrição')
    image = models.ImageField('Foto', upload_to='pictures/%Y/%m/%d', blank=True)
    category = models.CharField('Categoria', choices=categories, max_length=20, default='Outros')
    published = models.BooleanField('Publicado', default=False)
    registered_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self) -> str:
        return self.title
