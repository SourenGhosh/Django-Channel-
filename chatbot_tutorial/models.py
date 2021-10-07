import datetime
from django.db import models
from django.contrib.auth.models import User

class ButtonTracker(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	fat_count=models.IntegerField(default=0, null=True, blank=True)
	stupid_count=models.IntegerField(default=0, null=True, blank=True)
	dumb_count=models.IntegerField(default=0, null=True, blank=True)

	def __str__(self):
		return str(self.user)