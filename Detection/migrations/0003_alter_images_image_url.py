# Generated by Django 4.1.1 on 2022-09-12 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Detection', '0002_remove_images_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image_url',
            field=models.CharField(max_length=200),
        ),
    ]
