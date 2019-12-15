# python imports
import uuid

# django/rest_framwork imports
from django.db import models

# project level imports
from libs.models import TimeStampedModel


class Groups(TimeStampedModel):
	id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
	name = models.CharField(max_length=256,blank=False,unique=True)
	description=models.TextField(blank=True)


	def __str__(self):
		return "{id}".format(id=self.name)


class Products(TimeStampedModel):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	name = models.CharField(max_length=256)
	group = models.ForeignKey(Groups,on_delete=models.CASCADE)
	description = models.TextField(blank=True)
	price = models.IntegerField(blank=True)

	class Meta:
		unique_together = [['name', 'group']]
			

	def __str__(self):
		return "{id}".format(id=self.name)

	def modify(self, payload):
		"""
		This method will update tasks attributes
		"""
		for key, value in payload.items():
			setattr(self, key, value)
		self.save()
