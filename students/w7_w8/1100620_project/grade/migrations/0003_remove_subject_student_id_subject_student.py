# Generated by Django 4.2.7 on 2023-11-23 14:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grade', '0002_subject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='student_id',
        ),
        migrations.AddField(
            model_name='subject',
            name='student',
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to='grade.student'),
        ),
    ]
