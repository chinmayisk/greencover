from tastypie.resources import ModelResource, ALL
from tastypie.authorization import Authorization
from django.contrib.auth.models import User
from greencover.models import *
from tastypie import fields

class UserModel(ModelResource):
	class Meta:
		queryset = User.objects.all()
		resource_name = 'user'
		fields = ['username', 'first_name', 'last_name']
		allowed_methods = ['get']


class TreeModel(ModelResource):
	class Meta:
		queryset = Tree.objects.all()
		resource_name = 'tree'
		authorization= Authorization()

class AchievementModel(ModelResource):
	class Meta:
		queryset = Achievement.objects.all()
		resource_name = 'achievement'
		allowed_methods = ['get']
