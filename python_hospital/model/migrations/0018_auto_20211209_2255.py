# Generated by Django 3.2.9 on 2021-12-09 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0017_alter_visu_visu_values'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visu',
            name='visu_label',
            field=models.CharField(choices=[('age', 'age'), ('readmitted', 'readmitted'), ('A1Cresult', 'A1Cresult'), ('diabetesMed', 'diabetesMed'), ('max_glu_serum', 'glycemie max'), ('change', 'changement de médicament'), ('insulin', 'insulin')], default='READMITTED', max_length=30),
        ),
        migrations.AlterField(
            model_name='visu',
            name='visu_values',
            field=models.CharField(choices=[('COUNT', 'count'), ('readmitted', 'readmitted'), ('A1Cresult', 'A1Cresult'), ('max_glu_serum', 'glycemie max'), ('change', 'changement de médicament'), ('insulin', 'insulin')], default='COUNT', max_length=50),
        ),
    ]