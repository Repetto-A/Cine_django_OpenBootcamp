# Generated by Django 4.1.3 on 2023-05-12 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_movie_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='director',
            name='img',
            field=models.ImageField(default='steven.jpg', upload_to=''),
        ),
        migrations.AlterField(
            model_name='movie',
            name='img',
            field=models.ImageField(upload_to=''),
        ),
    ]
