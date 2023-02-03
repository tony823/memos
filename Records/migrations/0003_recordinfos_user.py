# Generated by Django 3.2.17 on 2023-02-02 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0006_auto_20230202_2138'),
        ('Records', '0002_alter_recordinfos_label'),
    ]

    operations = [
        migrations.AddField(
            model_name='recordinfos',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userInfo_id', to='Users.userinfos'),
        ),
    ]
