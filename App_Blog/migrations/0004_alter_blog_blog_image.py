# Generated by Django 3.2.4 on 2021-06-22 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Blog', '0003_rename_slug_content_blog_blog_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_image',
            field=models.ImageField(blank=True, null=True, upload_to='blog_images', verbose_name='Image'),
        ),
    ]
