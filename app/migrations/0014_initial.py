# Generated by Django 5.1.2 on 2024-10-28 15:09

import datetime
import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0013_remove_teacher_class_name_remove_exam_subject_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=100)),
                ('grade', models.IntegerField(choices=[(0, 'Kindergarten'), (1, 'Grade 1'), (2, 'Grade 2'), (3, 'Grade 3'), (4, 'Grade 4'), (5, 'Grade 5'), (6, 'Grade 6'), (7, 'Grade 7'), (8, 'Grade 8'), (9, 'Grade 9'), (10, 'Grade 10'), (11, 'Grade 11'), (12, 'Grade 12')])),
                ('student_count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('age', models.IntegerField()),
                ('grade', models.IntegerField(choices=[(0, 'Kindergarten'), (1, 'Grade 1'), (2, 'Grade 2'), (3, 'Grade 3'), (4, 'Grade 4'), (5, 'Grade 5'), (6, 'Grade 6'), (7, 'Grade 7'), (8, 'Grade 8'), (9, 'Grade 9'), (10, 'Grade 10'), (11, 'Grade 11'), (12, 'Grade 12')])),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=100)),
                ('photo', models.FileField(upload_to='image/student/')),
                ('password', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Myanmar', 'Myanmar'), ('English', 'English'), ('Mathematics', 'Mathematics'), ('Chemistry', 'Chemistry'), ('Physics', 'Physics'), ('Biology', 'Biology'), ('Economy', 'Economy'), ('Science', 'Science'), ('Geometry', 'Geometry'), ('History', 'History')], max_length=100)),
                ('grade', models.IntegerField(choices=[(0, 'Kindergarten'), (1, 'Grade 1'), (2, 'Grade 2'), (3, 'Grade 3'), (4, 'Grade 4'), (5, 'Grade 5'), (6, 'Grade 6'), (7, 'Grade 7'), (8, 'Grade 8'), (9, 'Grade 9'), (10, 'Grade 10'), (11, 'Grade 11'), (12, 'Grade 12')])),
                ('total_chapter', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Headmaster',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=100)),
                ('degree', models.CharField(max_length=200)),
                ('salary', models.IntegerField()),
                ('work_at', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('experience', models.TextField(blank=True)),
                ('photo', models.FileField(upload_to='image/teacher/')),
                ('password', models.IntegerField()),
                ('name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('test_taker_count', models.IntegerField()),
                ('grade', models.IntegerField(choices=[(0, 'Kindergarten'), (1, 'Grade 1'), (2, 'Grade 2'), (3, 'Grade 3'), (4, 'Grade 4'), (5, 'Grade 5'), (6, 'Grade 6'), (7, 'Grade 7'), (8, 'Grade 8'), (9, 'Grade 9'), (10, 'Grade 10'), (11, 'Grade 11'), (12, 'Grade 12')])),
                ('max_point', models.IntegerField(choices=[(100, '100'), (50, '50'), (25, '25')])),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=100)),
                ('degree', models.CharField(max_length=200)),
                ('salary', models.IntegerField()),
                ('work_at', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('experience', models.TextField(blank=True)),
                ('photo', models.FileField(upload_to='image/teacher/')),
                ('password', models.IntegerField()),
                ('class_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.class')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject', to='app.subject')),
            ],
        ),
    ]
