# Generated by Django 3.2.9 on 2021-12-09 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0016_alter_pred_medication'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visu',
            name='visu_values',
            field=models.CharField(choices=[('COUNT', 'count'), ('readmitted', 'readmitted'), ('A1Cresult', 'A1Cresult'), ('OTHER', 'other')], default='COUNT', max_length=50),
        ),
    ]