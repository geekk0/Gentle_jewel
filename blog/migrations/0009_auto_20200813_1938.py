# Generated by Django 3.0.4 on 2020-08-13 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_postimages_test_field'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Статьи блога'},
        ),
        migrations.AlterModelOptions(
            name='postimages',
            options={'verbose_name': 'Картинки к постам'},
        ),
    ]