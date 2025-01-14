# Generated by Django 4.2.14 on 2024-10-25 21:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aplicacao', '0009_alter_receita_modo_preparo_alter_receita_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='receita',
            name='sugestao',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='ReceitaSalva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saved_at', models.DateTimeField(auto_now_add=True)),
                ('receitaSalva', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacao.receita')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
