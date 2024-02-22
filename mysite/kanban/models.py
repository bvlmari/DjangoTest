# Create your models here.
import datetime

from django.db import models
from django.utils import timezone

class Task(models.Model):
	task_name = models.CharField(max_length=200)
	task_description = models.CharField(max_length=200)
	created_date = models.DateTimeField("date published")

	def __str__(self):
		return self.task_name
	
	def was_published_recently(self):
		return self.created_date >= timezone.now() - datetime.timedelta(days=1)

class state(models.Model):
	question = models.ForeignKey(Task, on_delete=models.CASCADE)
	state = models.CharField(max_length=30)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return self.state