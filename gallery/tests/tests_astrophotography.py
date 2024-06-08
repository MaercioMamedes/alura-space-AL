from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Astrophotography
from datetime import date
from django.core.exceptions import ValidationError

class AstrophotographyTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', password='12345')
    
    #cria um objeto astrophotography com todos os campos preenchidos e verifica se os valores estão corretos
    def test_create_astrophotography(self):
        astro = Astrophotography.objects.create(
            image_source='NASA',
            title='Nebulosa de Orion',
            date_image=date(2021, 1, 1),
            description='Uma imagem espetacular da Nebulosa de Orion.',
            category='Nebulosa',
            published=True,
            registered_by=self.user
        )
        self.assertEqual(astro.title, 'Nebulosa de Orion')
        self.assertEqual(astro.image_source, 'NASA')
        self.assertEqual(astro.category, 'Nebulosa')
        self.assertTrue(astro.published)
        self.assertEqual(astro.registered_by.username, 'testuser')

    #verifica se os valores padrões são atribuidos corretamente
    def test_default_values(self):
        astro = Astrophotography.objects.create(
            title='Via Láctea',
            description='Uma bela imagem da Via Láctea.',
            registered_by=self.user
        )
        #self.assertEqual(astro.date_image, date(2000, 1, 1))
        self.assertEqual(astro.date_image, '2000-01-01')
        self.assertEqual(astro.category, 'Outros')
        self.assertFalse(astro.published)
        
    #verifica se a criação de um objeto astrophotography falha quando o titulo excede 500 caracteres
    def test_title_max_length(self):
        title = 'a' * 501  # 501 characters
        astro = Astrophotography(
            title=title,
            description='Exceeding title length.',
            registered_by=self.user
        )
        with self.assertRaises(ValidationError):
            astro.full_clean()
    
    #verifica se as categorias permitidas podem ser atribuidas corretamente ao objeto astrophotography
    def test_valid_categories(self):
        valid_categories = ['Galáxia', 'Aglomerado', 'Estrela', 'Nebulosa', 'Planeta']
        for category in valid_categories:
            astro = Astrophotography.objects.create(
                title=f'Test {category}',
                description=f'Image of a {category}.',
                category=category,
                registered_by=self.user
            )
            self.assertEqual(astro.category, category)
    
    #verifica se o campo registered_by relaciona corretamente o objeto astrophotography ao usuario user
    def test_user_relation(self):
        astro = Astrophotography.objects.create(
            title='Supernova',
            description='Uma imagem incrível de uma supernova.',
            registered_by=self.user
        )
        self.assertEqual(astro.registered_by, self.user)

