# Generated by Django 3.2.4 on 2021-06-22 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(max_length=264, null=True, unique=True),
        ),
    ]
