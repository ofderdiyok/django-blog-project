# Generated by Django 4.0.5 on 2022-07-04 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
