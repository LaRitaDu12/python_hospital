# Generated by Django 3.2.9 on 2021-12-09 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0009_pred'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pred',
            name='gender',
            field=models.CharField(choices=[(1, 'female'), ('male', 'male'), ('unknown', 'unknown')], default='unknown', max_length=30),
        ),
    ]
