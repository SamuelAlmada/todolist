# Generated by Django 5.1 on 2024-09-03 00:49

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_task_remove_todolist_status_delete_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='custom_status',
        ),
        migrations.AddField(
            model_name='task',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('pending', 'Pendente'), ('in_progress', 'Em Progresso'), ('completed', 'Completo')], default='pending', max_length=50),
        ),
    ]
