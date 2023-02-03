# Generated by Django 3.2.17 on 2023-02-02 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0005_auto_20230202_2101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentinfos',
            name='classInfo',
        ),
        migrations.RemoveField(
            model_name='userinfos',
            name='classInfo',
        ),
        migrations.CreateModel(
            name='TeacherBindClassList',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('isProcess', models.BooleanField(default=False)),
                ('classes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacherBindClass_id', to='Users.classinfos')),
                ('teachers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_id', to='Users.userinfos')),
            ],
            options={
                'verbose_name': '教师绑定班级信息表',
                'verbose_name_plural': '教师绑定班级信息表',
            },
        ),
        migrations.CreateModel(
            name='StudentBindClassList',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('isProcess', models.BooleanField(default=False)),
                ('classes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studentBindClass_id', to='Users.classinfos')),
                ('students', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_id', to='Users.studentinfos')),
            ],
            options={
                'verbose_name': '学生绑定班级信息表',
                'verbose_name_plural': '学生绑定班级信息表',
            },
        ),
    ]
