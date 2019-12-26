# python imports
from datetime import datetime
import re,random

# Django Imports
from rest_framework import serializers
from rest_framework.validators import (
										UniqueValidator,
										UniqueTogetherValidator,
										)


# app level Imports
from .models import (
					Products,
					Groups,
					)


class GroupAddSerializer(serializers.ModelSerializer):
	created_at = serializers.DateTimeField(required=False)

	class Meta:
		model = Groups
		fields = '__all__'

	def create(self, validated_data):
		return Groups.objects.create(**validated_data)


class ListGroupSerializer(serializers.ModelSerializer):
	created_at = serializers.DateTimeField(required=False)

	class Meta:
		model = Groups
		fields = '__all__'



class GroupUpdateSerializer(serializers.ModelSerializer):
	name = serializers.CharField(required=False)

	class Meta:
		model = Groups
		fields = ('id',"name","description","is_active")


	def update(self, instance, validated_data):
		for attr, value in validated_data.items():
			setattr(instance, attr, value)
		instance.save()
		return instance

class GroupDeactivateSerializer(serializers.ModelSerializer):
	name = serializers.CharField(required=False)

	class Meta:
		model = Groups
		fields = ('id',"name","is_active")


	def update(self, instance, validated_data):
		instance.is_active = False
		instance.save()
		return instance


class ProductAddSerializer(serializers.ModelSerializer):
	created_at = serializers.DateTimeField(required=False)
	group = serializers.SlugRelatedField(
		slug_field='name',
		queryset=Groups.objects.all()
	 )

	class Meta:
		model = Products
		fields = '__all__'

	def create(self, validated_data):
		return Products.objects.create(**validated_data)


class ListProductSerializer(serializers.ModelSerializer):
	created_at = serializers.DateTimeField(required=False)
	group = serializers.SlugRelatedField(
		slug_field='name',
		queryset=Groups.objects.all()
	 )

	class Meta:
		model = Products
		fields = '__all__'



class ProductUpdateSerializer(serializers.ModelSerializer):
	group = serializers.SlugRelatedField(
		slug_field='name',
		queryset=Groups.objects.all(),
		required = False
	 )
	name = serializers.CharField(required=False)

	class Meta:
		model = Products
		fields = ('id',"name","description","price","is_active","group","model","serial_no")


	def update(self, instance, validated_data):
		for attr, value in validated_data.items():
			setattr(instance, attr, value)
		instance.save()
		return instance


class ProductDeactivateSerializer(serializers.ModelSerializer):
	name = serializers.CharField(required=False)

	class Meta:
		model = Products
		fields = ('id',"name","is_active")


	def update(self, instance, validated_data):
		instance.is_active = False
		instance.save()
		return instance

