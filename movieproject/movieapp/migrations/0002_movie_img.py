# Generated by Django 4.2.1 on 2023-05-29 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='aaaaa', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
