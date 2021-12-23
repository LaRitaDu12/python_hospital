# Generated by Django 3.2.9 on 2021-12-09 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0014_alter_pred_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pred',
            name='AC1result',
            field=models.IntegerField(choices=[(0, 'Over 7'), (1, 'Over 8'), (2, 'None'), (3, 'Norm')], default=2),
        ),
        migrations.AlterField(
            model_name='pred',
            name='admission_soucre',
            field=models.IntegerField(choices=[(0, 'Physician Referral'), (1, 'Clinic Referral'), (2, 'HMO Referral'), (3, 'Transfer from a hospital'), (4, 'Transfer from a Skilled Nursing Facility (SNF)'), (5, 'Transfer from another health care facility'), (6, 'Emergency Room'), (7, 'Court/Law Enforcement'), (8, 'Not Available'), (9, 'Transfer from critial access hospital'), (10, 'Normal Delivery'), (11, 'Sick Baby'), (12, 'Extramural Birth'), (13, 'NULL'), (14, 'Not Mapped'), (15, 'Transfer from hospital inpt/same fac reslt in a sep claim'), (16, 'Transfer from Ambulatory Surgery Center')], default=0),
        ),
        migrations.AlterField(
            model_name='pred',
            name='admission_type',
            field=models.IntegerField(choices=[(0, 'Emergency'), (1, 'Urgent'), (2, 'Elective'), (3, 'Newborn'), (4, 'Not Available'), (5, 'NULL'), (6, 'Trauma Center'), (7, 'Not Mapped')], default=4),
        ),
        migrations.AlterField(
            model_name='pred',
            name='age',
            field=models.IntegerField(choices=[(0, '0-10'), (1, '10-20'), (2, '20-30'), (3, '30-40'), (4, '40-50'), (5, '50-60'), (6, '60-70'), (7, '70-80'), (8, '80-90'), (9, '90-100')], default=3),
        ),
        migrations.AlterField(
            model_name='pred',
            name='change_medication',
            field=models.IntegerField(choices=[(0, 'Yes'), (1, 'No')], default=1),
        ),
        migrations.AlterField(
            model_name='pred',
            name='diabetes_med',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], default=0),
        ),
        migrations.AlterField(
            model_name='pred',
            name='diagnostique_1',
            field=models.IntegerField(choices=[(0, '?'), (1, 'Complications-of-Pregnancy-Childbirth-and-the-Puerperium'), (2, 'Congenital-Anomalies'), (3, 'Diseases-of-the-Blood-and-Blood-forming-Organs'), (4, 'Diseases-of-the-Circulatory-System'), (5, 'Diseases-of-the-Digestive-System'), (6, 'Diseases-of-the-Genitourinary-System'), (7, 'Diseases-of-the-Musculoskeletal-System-and-Connective-Tissue'), (8, 'Diseases-of-the-Nervous-System-and-Sense-Organs'), (9, 'Diseases of the Respiratory System'), (10, 'Diseases of the Skin and Subcutaneous Tissue'), (11, 'Endocrine, Nutritional and Metabolic Diseases, and Immunity Disorders'), (12, 'Infectious and Parasitic Diseases'), (13, 'Injury and Poisoning'), (14, 'Mental Disorders'), (15, 'Neoplasms'), (16, 'Supplementary Classification of External Causes of Injury and Poisoning'), (17, 'Supplementary Classification of Factors influencing Health Status and Contact with Health Services'), (18, 'Symptoms, Signs and Ill-defined Conditions')], default=11),
        ),
        migrations.AlterField(
            model_name='pred',
            name='diagnostique_2',
            field=models.IntegerField(choices=[(0, '?'), (1, 'Complications-of-Pregnancy-Childbirth-and-the-Puerperium'), (2, 'Congenital-Anomalies'), (3, 'Diseases-of-the-Blood-and-Blood-forming-Organs'), (4, 'Diseases-of-the-Circulatory-System'), (5, 'Diseases-of-the-Digestive-System'), (6, 'Diseases-of-the-Genitourinary-System'), (7, 'Diseases-of-the-Musculoskeletal-System-and-Connective-Tissue'), (8, 'Diseases-of-the-Nervous-System-and-Sense-Organs'), (9, 'Diseases of the Respiratory System'), (10, 'Diseases of the Skin and Subcutaneous Tissue'), (11, 'Endocrine, Nutritional and Metabolic Diseases, and Immunity Disorders'), (12, 'Infectious and Parasitic Diseases'), (13, 'Injury and Poisoning'), (14, 'Mental Disorders'), (15, 'Neoplasms'), (16, 'Supplementary Classification of External Causes of Injury and Poisoning'), (17, 'Supplementary Classification of Factors influencing Health Status and Contact with Health Services'), (18, 'Symptoms, Signs and Ill-defined Conditions')], default=0),
        ),
        migrations.AlterField(
            model_name='pred',
            name='diagnostique_3',
            field=models.IntegerField(choices=[(0, '?'), (1, 'Complications-of-Pregnancy-Childbirth-and-the-Puerperium'), (2, 'Congenital-Anomalies'), (3, 'Diseases-of-the-Blood-and-Blood-forming-Organs'), (4, 'Diseases-of-the-Circulatory-System'), (5, 'Diseases-of-the-Digestive-System'), (6, 'Diseases-of-the-Genitourinary-System'), (7, 'Diseases-of-the-Musculoskeletal-System-and-Connective-Tissue'), (8, 'Diseases-of-the-Nervous-System-and-Sense-Organs'), (9, 'Diseases of the Respiratory System'), (10, 'Diseases of the Skin and Subcutaneous Tissue'), (11, 'Endocrine, Nutritional and Metabolic Diseases, and Immunity Disorders'), (12, 'Infectious and Parasitic Diseases'), (13, 'Injury and Poisoning'), (14, 'Mental Disorders'), (15, 'Neoplasms'), (16, 'Supplementary Classification of External Causes of Injury and Poisoning'), (17, 'Supplementary Classification of Factors influencing Health Status and Contact with Health Services'), (18, 'Symptoms, Signs and Ill-defined Conditions')], default=0),
        ),
        migrations.AlterField(
            model_name='pred',
            name='discharge',
            field=models.IntegerField(choices=[(0, 'Discharged to home'), (1, 'Discharged/transferred to another short term'), (2, 'Discharged/transferred to SNF'), (3, 'Discharged/transferred to ICF'), (4, 'Discharged/transferred to another type of inpatient'), (5, 'Discharged/transferred to home with home health'), (6, 'Left AMA'), (7, 'Discharged/transferred to home under care of Home'), (8, 'Admitted as an inpatient to this hospital'), (9, 'Neonate discharged to another hospital for neonatal aftercare'), (10, 'Still patient or expected to return for outpatient services'), (11, 'Discharged/transferred within this institution to Medicare approved swing bed'), (12, 'Discharged/transferred/referred another institution for outpatient services'), (13, 'Discharged/transferred/referred to this institution for outpatient services'), (14, 'NULL'), (15, 'Discharged/transferred to another rehab fac including rehab units of a hospital'), (16, 'Discharged/transferred to a long term care hospital.'), (17, 'Discharged/transferred to a nursing facility certified under Medicaid but not certified under Medicare.'), (18, 'Not Mapped'), (19, 'Discharged/transferred to a federal health care facility.'), (20, 'Discharged/transferred/referred to a psychiatric hospital of psychiatric distinct part unit of a hospital')], default=0),
        ),
        migrations.AlterField(
            model_name='pred',
            name='max_glue',
            field=models.IntegerField(choices=[(0, 'Over 200'), (1, 'Over 300'), (2, 'None'), (3, 'Norm')], default=2),
        ),
        migrations.AlterField(
            model_name='pred',
            name='medication',
            field=models.IntegerField(choices=[(0, 'metformin_Down'), (1, 'metformin_No'), (2, 'metformin_Steady'), (3, 'metformin_Up'), (4, 'repaglinide_Down'), (5, 'repaglinide_No'), (6, 'repaglinide_Steady'), (7, 'repaglinide_Up'), (8, 'nateglinide_Down'), (9, 'nateglinide_No'), (10, 'nateglinide_Steady'), (11, 'nateglinide_Up'), (12, 'chlorpropamide_Down'), (13, 'chlorpropamide_No'), (14, 'chlorpropamide_Steady'), (15, 'chlorpropamide_Up'), (16, 'glimepiride_Down'), (17, 'glimepiride_No'), (18, 'glimepiride_Steady'), (19, 'glimepiride_Up'), (20, 'acetohexamide_No'), (21, 'acetohexamide_Steady'), (22, 'glipizide_Down'), (23, 'glipizide_No'), (24, 'glipizide_Steady'), (25, 'glipizide_Up'), (26, 'glyburide_Down'), (27, 'glyburide_No'), (28, 'glyburide_Steady'), (29, 'glyburide_Up'), (30, 'tolbutamide_No'), (31, 'tolbutamide_Steady'), (32, 'pioglitazone_Down'), (33, 'pioglitazone_No'), (34, 'pioglitazone_Steady'), (35, 'pioglitazone_Up'), (36, 'rosiglitazone_Down'), (37, 'rosiglitazone_No'), (38, 'rosiglitazone_Steady'), (39, 'rosiglitazone_Up'), (40, 'acarbose_No'), (41, 'acarbose_Steady'), (42, 'acarbose_Up'), (43, 'miglitol_Down'), (44, 'miglitol_No'), (45, 'miglitol_Steady'), (46, 'miglitol_Up'), (47, 'troglitazone_No'), (48, 'troglitazone_Steady'), (49, 'tolazamide_No'), (50, 'tolazamide_Steady'), (51, 'insulin_Down'), (52, 'insulin_No'), (53, 'insulin_Steady'), (54, 'insulin_Up'), (55, 'glyburide-metformin_Down'), (56, 'glyburide-metformin_No'), (57, 'glyburide-metformin_Steady'), (57, 'glyburide-metformin_Up'), (58, 'glipizide-metformin_No'), (59, 'glipizide-metformin_Steady'), (60, 'glimepiride-pioglitazone_No'), (61, 'metformin-rosiglitazone_No'), (62, 'metformin-rosiglitazone_Steady'), (63, 'metformin-pioglitazone_No'), (64, 'metformin-pioglitazone_Steady')], default=54),
        ),
        migrations.AlterField(
            model_name='pred',
            name='speciality',
            field=models.IntegerField(choices=[(0, '?'), (1, 'Allergy and Immunology'), (2, 'Anesthesiology'), (3, 'Anesthesiology-Pediatric'), (4, 'Cardiology'), (5, 'Cardiology-Pediatric'), (6, 'DCPTEAM'), (7, 'Dentistry'), (8, 'Dermatology'), (9, 'Emergency/Trauma'), (10, 'Endocrinology'), (11, 'Endocrinology-Metabolism'), (12, 'Family/GeneralPractice'), (13, 'Gastroenterology'), (14, 'Gynecology'), (15, 'Hematology'), (16, 'Hematology/Oncology'), (17, 'Hospitalist'), (18, 'InfectiousDiseases'), (19, 'InternalMedicine'), (20, 'Nephrology'), (21, 'Neurology'), (22, 'Neurophysiologie'), (23, 'Obsterics&Gynecology-GynecologicOnco'), (24, 'Obstetrics'), (25, 'ObstetricsandGynecology'), (26, 'Oncology'), (27, 'Ophthalmology'), (28, 'Orthopedics'), (29, 'Orthopedics-Reconstructive'), (30, 'Osteopath'), (31, 'Otolaryngology'), (32, 'OutreachServices'), (33, 'Pathology'), (34, 'Pediatrics'), (35, 'Pediatrics-CriticalCare'), (36, 'Pediatrics-EmergencyMedicine'), (37, 'Pediatrics-Endocrinology'), (38, 'Pediatrics-Hematology-Oncology'), (39, 'Pediatrics-Neurology'), (40, 'Pediatrics-Pulmonology'), (41, 'Perinatology'), (42, 'PhysicalMedicineandRehabilitation'), (43, 'PhysicianNotFound'), (44, 'Podiatry'), (45, 'Proctology'), (46, 'Psychiatry'), (47, 'Psychiatry-Addictive'), (48, 'Psychiatry-Child/Adolescent'), (49, 'Psychology'), (50, 'Pulmonology'), (51, 'Radiologist'), (52, 'Radiology'), (53, 'Resident'), (54, 'Rheumatology'), (55, 'Speech'), (56, 'SportsMedicine'), (57, 'Surgeon'), (58, 'Surgery-Cardiovascular'), (59, 'Surgery-Cardiovascular/Thoracic'), (60, 'Surgery-Colon&Rectal'), (61, 'Surgery-General'), (62, 'Surgery-Maxillofacial'), (63, 'Surgery-Neuro'), (64, 'Surgery-Pediatric'), (65, 'Surgery-Plastic'), (66, 'Surgery-PlasticwithinHeadandNeck'), (67, 'Surgery-Thoracic'), (68, 'Surgery-Vascular'), (69, 'SurgicalSpecialty'), (70, 'Urology')], default=12),
        ),
    ]