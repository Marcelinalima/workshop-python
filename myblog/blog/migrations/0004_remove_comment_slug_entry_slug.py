# Generated by Django 4.2.4 on 2023-08-18 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='slug',
        ),
        migrations.AddField(
            model_name='entry',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]