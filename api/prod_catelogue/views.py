# Django Imports
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.decorators import action


# Projects Imports
from libs.constants import (
		BAD_REQUEST,
		BAD_ACTION,
		OPERATION_NOT_ALLOWED,
)
# from accounts.constants import COULD_NOT_SEND_OTP, USER_NOT_REGISTERED
from libs.exceptions import (
					ParseException,
					ResourceNotFoundException,
					BadRequestException,
				)

# app level imports
from .services import (
						GroupsService,
						ProductsService,
					)
from .serializers import (
	ProductAddSerializer,
	ListProductSerializer,
	ProductUpdateSerializer,
	GroupAddSerializer,
	ListGroupSerializer,
	GroupUpdateSerializer,
	GroupDeactivateSerializer,
	ProductDeactivateSerializer
)

class GroupManager(viewsets.ModelViewSet):
	"""
	api's to manage the groups
	"""
	http_method_names = ['get', 'post', 'put','delete']

	serializers_dict = {
		'addgroup': GroupAddSerializer,
		'grouplist': ListGroupSerializer,
		"updategroup":GroupUpdateSerializer,
		"deletegroup":GroupDeactivateSerializer,
	}

	def get_queryset(self,filterdata=None):
		return GroupsService.get_queryset(filterdata)


	def get_serializer_class(self):
		"""
		"""
		try:
			return self.serializers_dict[self.action]
		except KeyError as key:
			raise ParseException(BAD_ACTION, errors=key)
			


	@action(
		methods=['post'],
		detail=False)
	def addgroup(self, request, format='json'):
		"""
		this will add the group
		"""
		data = request.data
		serializer = self.get_serializer(data = data)
		if serializer.is_valid():
			user = serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			raise BadRequestException(BAD_REQUEST,serializer.errors)

	@action(
		methods=['get'],
		detail=False,
		)
	def grouplist(self, request, format='json'):
		"""
		list of all groups with pagination
		"""
		page = self.paginate_queryset(self.get_queryset())
		serializer = self.get_serializer(page,many=True)
		return self.get_paginated_response(serializer.data)


	@action(
		methods=['delete'],
		detail=False,
		)
	def deletegroup(self, request,  format='json'):
		"""
		deactivate the group on group id,
		if not then it will raise bad_request
		"""
		try:
			Group_id = request.GET.get("id")
			data_object = GroupsService.get_instance(Group_id)
			serializer = self.get_serializer(data_object,data = {})
			if serializer.is_valid():
				user = serializer.save()
				return Response({"status":"group has been deactivated"}, status=status.HTTP_200_OK)
			else:
				raise BadRequestException(BAD_REQUEST,serializer.errors)
		except:
			raise BadRequestException(OPERATION_NOT_ALLOWED)

	@action(
		methods=['put'], 
		detail=False, 
		)
	def updategroup(self, request, format='json'):
		"""
		update the group on group id,
		if not then it will raise bad_request
		"""
		try:
			data = request.data
			data_object = GroupsService.get_instance(data["id"])
			serializer = self.get_serializer(data_object,data = data)
			if serializer.is_valid():
				user = serializer.save()
				return Response(serializer.data, status=status.HTTP_200_OK)
			else:
				raise BadRequestException(BAD_REQUEST,serializer.errors)
		except:

			raise BadRequestException(OPERATION_NOT_ALLOWED)




class ProductManager(viewsets.ModelViewSet):
	"""
	api's to manage the products
	"""
	http_method_names = ['get', 'post', 'put','delete']

	serializers_dict = {
		'addproduct': ProductAddSerializer,
		'productlist': ListProductSerializer,
		"updateproduct":ProductUpdateSerializer,
		"deleteproduct":ProductDeactivateSerializer,
	}

	def get_queryset(self,filterdata=None):
		return ProductsService.get_queryset(filterdata)


	def get_serializer_class(self):
		"""
		"""
		try:
			return self.serializers_dict[self.action]
		except KeyError as key:
			raise ParseException(BAD_ACTION, errors=key)
			


	@action(
		methods=['post'],
		detail=False,
		)
	def addproduct(self, request, format='json'):
		"""
		adding the new product,
		if there is no given group then it will create new and
		""" 
		try:
			data = request.data
			group_name = data.pop('group')
			data["group"] = GroupsService.get_or_create(group_name)
			serializer = self.get_serializer(data = data)
			if serializer.is_valid():
				user = serializer.save()
				return Response(serializer.data, status=status.HTTP_201_CREATED)
			else:
				raise BadRequestException(BAD_REQUEST,serializer.errors)
		except:
			raise BadRequestException(BAD_REQUEST)

	@action(
		methods=['get'],
		detail=False,
		)
	def productlist(self, request, format='json'):
		"""
		list of all products with pagination
		"""
		page = self.paginate_queryset(self.get_queryset())
		serialiser = self.get_serializer(page,many=True)
		return self.get_paginated_response(serialiser.data)


	@action(
		methods=['delete'],
		detail=False,
		)
	def deleteproduct(self, request,  format='json'):
		"""
		deactivate the product,
		if not then it will raise bad_request
		"""
		try:
			product_id = request.GET.get("id")
			data_object = ProductsService.get_instance(product_id)
			serializer = self.get_serializer(data_object,data = {})
			if serializer.is_valid():
				user = serializer.save()
				return Response({"status": "product has been deactivated"}, status=status.HTTP_200_OK)
			else:
				raise BadRequestException(BAD_REQUEST,serializer.errors)
		except self.model.DoesNotExist:
			raise ResourceNotFoundException(BAD_REQUEST)
		except:
			raise BadRequestException(OPERATION_NOT_ALLOWED)

	@action(
		methods=['put'], 
		detail=False, 
		)
	def updateproduct(self, request, format='json'):
		"""
		update the product on product id,
		if not then it will raise bad_request
		"""
		try:
			data = request.data
			data_object = ProductsService.get_instance(data["id"])
			serializer = self.get_serializer(data_object,data = data)
			if serializer.is_valid():
				user = serializer.save()
				return Response(serializer.data, status=status.HTTP_200_OK)
			else:
				raise BadRequestException(BAD_REQUEST,serializer.errors)
		except:
			raise BadRequestException(OPERATION_NOT_ALLOWED)

	@action(methods=['get'], detail=False)
	def groupanalysis(self, request):
		"""
		analyzing the group wise data
		"""
		try:
			return Response(ProductsService.get_group_analysis())
		except:
			raise ParseException(BAD_REQUEST)









