# Generated by Django 4.2.7 on 2023-11-25 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grade', '0003_remove_subject_student_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='student',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='grade.student'), # type: ignore
        ),
    ]
