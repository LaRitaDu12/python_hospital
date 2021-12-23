# Generated by Django 3.2.9 on 2021-12-10 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0019_auto_20211210_0124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visu',
            name='visu_label',
            field=models.CharField(choices=[('age', 'age'), ('readmitted', 'readmitted'), ('A1Cresult', 'A1Cresult'), ('diabetesMed', 'diabetesMed'), ('max_glu_serum', 'glycemie max'), ('change', 'changement de médicament'), ('insulin', 'insulin'), ('acetohexamide', 'acetohexamide')], default='READMITTED', max_length=30),
        ),
        migrations.AlterField(
            model_name='visu',
            name='visu_values',
            field=models.CharField(choices=[('COUNT', 'count'), ('readmitted', 'readmitted'), ('A1Cresult', 'A1Cresult'), ('max_glu_serum', 'glycemie max'), ('change', 'changement de médicament'), ('insulin', 'insulin'), ('acetohexamide', 'acetohexamide')], default='COUNT', max_length=50),
        ),
    ]
