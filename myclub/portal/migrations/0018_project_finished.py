# Generated by Django 2.1.2 on 2018-11-26 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0017_auto_20181122_1450'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='finished',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=30, null=True),
        ),
    ]