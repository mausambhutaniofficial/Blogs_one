# Generated by Django 3.0.8 on 2020-07-31 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200731_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default', upload_to='profile_pics'),
        ),
    ]