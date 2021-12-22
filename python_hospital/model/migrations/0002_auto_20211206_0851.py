# Generated by Django 3.2.9 on 2021-12-06 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visu',
            name='visu_label',
            field=models.CharField(choices=[('AGE', 'age'), ('TIME_IN_HOSPITAL', 'time_in_hospital'), ('READMITTED', 'readmitted'), ('A1CRESULT', 'A1Cresult'), ('DIABETESMED', 'diabetesMed')], default='READMITTED', max_length=30),
        ),
        migrations.AlterField(
            model_name='visu',
            name='visu_values',
            field=models.CharField(choices=[('COUNT', 'count'), ('TIME_IN_HOSPITAL', 'time_in_hospital'), ('NUMBER_OF_MEDICATION', 'number_of_medication')], default='COUNT', max_length=50),
        ),
    ]