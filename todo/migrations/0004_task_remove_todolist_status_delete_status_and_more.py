# Generated by Django 5.1 on 2024-08-29 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_status_todolist_delete_task'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('in_progress', 'In Progress'), ('completed', 'Completed'), ('custom', 'Custom')], default='pending', max_length=50)),
                ('custom_status', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='todolist',
            name='status',
        ),
        migrations.DeleteModel(
            name='Status',
        ),
        migrations.DeleteModel(
            name='TodoList',
        ),
    ]
