# Generated by Django 4.0.3 on 2022-03-29 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_article_scopes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scope',
            options={'verbose_name': 'Тэг', 'verbose_name_plural': 'Тэги'},
        ),
    ]