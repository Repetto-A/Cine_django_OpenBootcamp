# Generated by Django 4.1.3 on 2023-05-12 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_movie_release_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='release_year',
            field=models.IntegerField(),
        ),
    ]
