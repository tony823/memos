# Generated by Django 3.2.17 on 2023-02-02 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_classinfos_gradeinfos_schoolinfos'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentinfos',
            name='classInfo',
            field=models.ManyToManyField(related_name='class_id', to='Users.ClassInfos'),
        ),
        migrations.AddField(
            model_name='userinfos',
            name='classInfo',
            field=models.ManyToManyField(related_name='jionClass_id', to='Users.ClassInfos'),
        ),
    ]
