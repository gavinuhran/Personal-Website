# Generated by Django 3.0.5 on 2020-05-12 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_auto_20200512_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='description1',
            field=models.TextField(default='placeholder'),
        ),
        migrations.AddField(
            model_name='profile',
            name='description2',
            field=models.TextField(default='placeholder'),
        ),
    ]