# Generated by Django 2.0.3 on 2018-04-08 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0005_student_teacher'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='username',
            new_name='courseCode',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='course',
        ),
        migrations.AddField(
            model_name='feedback',
            name='prn',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher',
            name='courseCode',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
