# Generated by Django 5.1.1 on 2024-10-01 14:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WachatMsgServer', '0002_wechatmessage_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='phone_data',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='WachatMsgServer.phonedata'),
        ),
    ]
