# Generated by Django 3.2.5 on 2021-08-12 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20210809_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professional',
            name='image',
            field=models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics'),
        ),
    ]
