# Generated by Django 5.1.2 on 2024-10-27 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_test_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='subjectmodel',
            name='teacher',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]