# Generated by Django 4.2.7 on 2024-02-08 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LongStoryApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='story',
            name='story',
        ),
        migrations.AddField(
            model_name='story',
            name='story_shown',
            field=models.TextField(default=False),
        ),
    ]
