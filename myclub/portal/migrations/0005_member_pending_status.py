# Generated by Django 2.1.2 on 2018-10-16 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0004_pending_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='pending_status',
            field=models.BooleanField(default=True),
        ),
    ]
