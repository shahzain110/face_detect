# Generated by Django 4.1.1 on 2022-09-13 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Detection', '0005_rename_images_images_db'),
    ]

    operations = [
        migrations.CreateModel(
            name='image_db',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='images_db',
        ),
    ]