# Generated by Django 3.2.9 on 2021-12-06 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0003_auto_20211206_0918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visu',
            name='visu_label',
            field=models.CharField(choices=[('AGE', 'age'), ('TIME_IN_HOSPITAL', 'time_in_hospital'), ('READMITTED', 'readmitted'), ('A1CRESULT', 'A1Cresult'), ('diabetesMed', 'diabetesMed')], default='READMITTED', max_length=30),
        ),
    ]
