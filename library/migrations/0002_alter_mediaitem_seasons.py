# Generated by Django 5.2 on 2025-05-07 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediaitem',
            name='seasons',
            field=models.PositiveIntegerField(default=1, verbose_name='Сезон'),
        ),
    ]
