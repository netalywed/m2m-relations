# Generated by Django 4.0.3 on 2022-04-01 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0012_remove_scope_is_main_articlescope_is_main'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlescope',
            name='is_main',
            field=models.BooleanField(verbose_name='Основной'),
        ),
    ]
