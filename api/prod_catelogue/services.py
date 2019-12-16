# Django Imports
from django.db.models import (
								Count,
								Sum,
								)


# app level Imports
from .models import (
					Products,
					Groups,
					)

# Projects Imports
from libs.constants import (
		BAD_REQUEST,
		BAD_ACTION,
		OPERATION_NOT_ALLOWED,
)
from libs.exceptions import (
					ParseException,
					ResourceNotFoundException,
					BadRequestException,
				)

class GroupsService(object):
	'''Service layer for the groups model'''

	@classmethod
	def get_queryset(cls, filter_data = None):
		"""
		fetching the group queryset on product id
		"""
		queryset = Groups.objects.all()
		if filter_data:
			try:
				queryset = queryset.filter(**filter_data)
			except:
				raise ParseException(BAD_REQUEST)
		return queryset
		
	@classmethod
	def get_instance(cls,group_id):
		"""
		fetching the group instance on product id
		"""
		try:
			return Groups.objects.get(id=group_id)
		except Groups.DoesNotExist:
			raise ResourceNotFoundException(BAD_REQUEST)

	@classmethod
	def get_or_create(cls,group_name,description=None):
		"""
		get or create the group on group name
		"""
		try:
			instance,created = Groups.objects.get_or_create(name=group_name)
			return instance
		except:
			raise ParseException(BAD_REQUEST)



class ProductsService(object):
	'''Service layer for the groups model'''

	@classmethod
	def get_queryset(cls, filter_data = None):
		"""
		fetching the product queryset on product id
		"""
		queryset = Products.objects.all()
		if filter_data:
			try:
				queryset = queryset.filter(**filter_data)
			except:
				raise ParseException(BAD_REQUEST)
		return queryset
		
	@classmethod
	def get_instance(cls,product_id):
		"""
		fetching the product instance on product id
		"""
		try:
			return Products.objects.get(id=product_id)
		except Products.DoesNotExist:
			raise ResourceNotFoundException(BAD_REQUEST)

	@classmethod
	def get_group_analysis(cls):
		"""
		Product analysis data
		"""
		product_rates = Products.objects.select_related('group').values('group__name').annotate(
				products_count=Count('price'),products_value = Sum('price')).order_by("group")
		return product_rates

	

