# Generated by Django 3.2.17 on 2023-02-02 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RoleInfos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('roleName', models.CharField(choices=[('家长', '家长'), ('教师', '教师')], max_length=20, verbose_name='角色名称')),
            ],
            options={
                'verbose_name': '角色信息',
                'verbose_name_plural': '角色信息',
            },
        ),
        migrations.CreateModel(
            name='UserInfos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nicName', models.CharField(max_length=20, verbose_name='用户昵称')),
                ('roles', models.ManyToManyField(related_name='role_id', to='Users.RoleInfos')),
            ],
            options={
                'verbose_name': '用户信息',
                'verbose_name_plural': '用户信息',
            },
        ),
    ]