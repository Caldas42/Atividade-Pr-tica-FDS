# Generated by Django 5.1.1 on 2024-09-27 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacao', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='receita',
            name='ingredientes',
            field=models.TextField(default='Ingredientes não informados'),
        ),
        migrations.AddField(
            model_name='receita',
            name='modo_preparo',
            field=models.TextField(default='Ingredientes não informados'),
        ),
    ]