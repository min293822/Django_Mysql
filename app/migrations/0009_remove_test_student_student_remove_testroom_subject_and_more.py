# Generated by Django 5.1.2 on 2024-10-28 03:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_subjectmodel_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test_student',
            name='student',
        ),
        migrations.RemoveField(
            model_name='testroom',
            name='subject',
        ),
        migrations.RemoveField(
            model_name='test_student',
            name='testroom',
        ),
        migrations.DeleteModel(
            name='StudentModel',
        ),
        migrations.DeleteModel(
            name='SubjectModel',
        ),
        migrations.DeleteModel(
            name='Test_student',
        ),
        migrations.DeleteModel(
            name='TestRoom',
        ),
    ]
