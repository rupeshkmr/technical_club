# Generated by Django 2.1.2 on 2018-10-28 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0013_member_pending_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='project',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='portal.Project'),
        ),
    ]