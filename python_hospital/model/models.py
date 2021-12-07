from django.db import models

class Visu(models.Model):
	visu_type = models.CharField(max_length=200)
	visu_title = models.CharField(max_length=200)
	visu_label_title = models.CharField(max_length=200, default='---')
	visu_description = models.TextField(default='---')

	ZONES_CHOICES = (
	("INFO", "info"),
	("COMPRENDRE", "comprendre"),
    ("IMPACT", "impact"))
	visu_zone = models.CharField(max_length=30,
                  choices=ZONES_CHOICES,
                  default="INFO")
	

	LABELS_CHOICES = (
	("age", "age"),
	("time_in_hospital", "time_in_hospital"),
    ("readmitted", "readmitted"),
    ("A1Cresult", "A1Cresult"),
    ("diabetesMed","diabetesMed"))
	visu_label = models.CharField(max_length=30,
                  choices=LABELS_CHOICES,
                  default="READMITTED")
	
	VALUES_CHOICES = (
	("COUNT","count"),
    ("time_in_hospital", "time_in_hospital"),
    ("number_of_medication", "number_of_medication"))
	visu_values = models.CharField(max_length=50,
                  choices=VALUES_CHOICES,
                  default="COUNT")

	def __str__(self):
		return self.visu_title