# Generated by Django 3.2.17 on 2023-02-02 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentInfos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('studentName', models.CharField(max_length=20, verbose_name='学生姓名')),
                ('userName', models.ManyToManyField(related_name='user_id', to='Users.UserInfos')),
            ],
            options={
                'verbose_name': '学生信息',
                'verbose_name_plural': '学生信息',
            },
        ),
    ]