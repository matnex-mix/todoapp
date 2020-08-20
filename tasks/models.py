from django.db import models

# Create your models here.

class Task(models.Model):
	title = models.CharField(max_length=50)
	description = models.CharField(max_length=2000)
	complete = models.BooleanField(default=False)
	due = models.DateTimeField()
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title
