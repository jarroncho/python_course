

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grade', '0006_course_delete_subject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='score',
        ),
    ]
