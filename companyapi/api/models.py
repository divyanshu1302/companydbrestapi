from __future__ import unicode_literals

from django.db import models

class employees(models.Model):
	first_name = models.CharField(max_length= 10)
	last_name = models.CharField(max_length= 10)
	e_id = models.IntegerField()

	def _str_(self):
		return self.first_name

# Create your models here.
