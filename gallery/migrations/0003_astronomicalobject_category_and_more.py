# Generated by Django 4.1 on 2023-03-22 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gallery", "0002_rename_objectastronomic_astronomicalobject"),
    ]

    operations = [
        migrations.AddField(
            model_name="astronomicalobject",
            name="category",
            field=models.CharField(
                choices=[
                    ("Galáxia", "Galáxia"),
                    ("Aglomerado", "Aglomerado"),
                    ("Estrela", "Estrela"),
                    ("Nebulosa", "Nebulosa"),
                    ("Planeta", "Planeta"),
                    ("Outros", "Outros"),
                ],
                default="Outros",
                max_length=20,
                verbose_name="Categoria",
            ),
        ),
        migrations.AddField(
            model_name="astronomicalobject",
            name="published",
            field=models.BooleanField(default=False, verbose_name="Publicado"),
        ),
    ]
