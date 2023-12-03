# Generated by Django 4.2.7 on 2023-11-30 12:22

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grade', '0005_remove_student_student_id_student_chinese_score_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(validators=[django.core.validators.MaxValueValidator(limit_value=100)])),
                ('chinese_score', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(limit_value=100)])),
                ('english_score', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(limit_value=100)])),
                ('math_score', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(limit_value=100)])),
                ('physics_score', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(limit_value=100)])),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='course', to='grade.student')),
            ],
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
    ]
