

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grade', '0003_remove_subject_student_id_subject_student'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Subject',
        ),
    ]
