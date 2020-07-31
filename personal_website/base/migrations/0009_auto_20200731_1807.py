# Generated by Django 3.0.5 on 2020-07-31 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_aboutme'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='featuredproject',
            name='url',
        ),
        migrations.AlterField(
            model_name='featuredproject',
            name='thumbnail',
            field=models.ImageField(blank=True, default='default.png', upload_to='media/featuredProjectIcons'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(blank=True, default='default.png', upload_to='media/profilePics'),
        ),
    ]
