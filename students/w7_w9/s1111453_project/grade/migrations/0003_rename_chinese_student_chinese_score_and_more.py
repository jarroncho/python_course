# Generated by Django 5.0 on 2023-12-14 10:21

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("grade", "0002_course"),
    ]

    operations = [
        migrations.RenameField(
            model_name="student",
            old_name="chinese",
            new_name="chinese_score",
        ),
        migrations.RenameField(
            model_name="student",
            old_name="english",
            new_name="english_score",
        ),
        migrations.RenameField(
            model_name="student",
            old_name="math",
            new_name="math_score",
        ),
        migrations.RenameField(
            model_name="student",
            old_name="physics",
            new_name="physics_score",
        ),
    ]
