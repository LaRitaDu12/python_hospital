# Generated by Django 3.2.9 on 2021-12-09 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0006_auto_20211206_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visu',
            name='visu_values',
            field=models.CharField(choices=[('COUNT', 'count'), ('time_in_hospital', 'time_in_hospital'), ('readmitted', 'readmitted'), ('number_of_medication', 'number_of_medication')], default='COUNT', max_length=50),
        ),
    ]
