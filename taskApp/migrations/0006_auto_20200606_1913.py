# Generated by Django 3.0.5 on 2020-06-06 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskApp', '0005_todo_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='content',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='title',
            field=models.TextField(max_length=100, null=True),
        ),
    ]
