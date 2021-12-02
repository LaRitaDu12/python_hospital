from django.db import models

class Visu(models.Model):
	visu_type = models.CharField(max_length=200)
	visu_zone = models.CharField(max_length=200)
	visu_dataset = models.CharField(max_length=200)
	visu_title = models.CharField(max_length=200)

	LABELS_CHOICES = (
    ("READMITTED", "readmitted"),
    ("A1CRESULT", "A1Cresult"))
	visu_label = models.CharField(max_length=30,
                  choices=LABELS_CHOICES,
                  default="READMITTED")
	
	VALUES_CHOICES = (
    ("TIME_IN_HOSPITAL", "time_in_hospital"),
    ("NUMBER_OF_MEDICATION", "number_of_medication"))
	visu_values = models.CharField(max_length=50,
                  choices=VALUES_CHOICES,
                  default="TIME_IN_HOSPITAL")

	def __str__(self):
		return self.visu_title