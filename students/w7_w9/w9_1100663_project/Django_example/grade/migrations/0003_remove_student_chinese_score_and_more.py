# Generated by Django 5.0 on 2023-12-27 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grade', '0002_remove_student_student_id_student_chinese_score_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='chinese_score',
        ),
        migrations.RemoveField(
            model_name='student',
            name='english_score',
        ),
        migrations.RemoveField(
            model_name='student',
            name='math_score',
        ),
        migrations.RemoveField(
            model_name='student',
            name='physics_score',
        ),
    ]
