from django.db import models


# Create your models here.
class Bookmark(models.Model):
	title = models.CharField(max_length=100, blank=True, null=True)
	url = models.URLField('url', unique=True)
	create_date = models.DateTimeField('Create Date', auto_now_add=True, blank=True, null=True)
	modify_date = models.DateTimeField('Modify Date', auto_now=True, blank=True, null=True)

	def __str__(self):
		return self.title
