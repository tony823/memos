# Generated by Django 3.2.17 on 2023-02-02 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0006_auto_20230202_2138'),
        ('Records', '0006_labelinfos_userinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labelinfos',
            name='userInfo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creater_id', to='Users.userinfos'),
        ),
    ]
