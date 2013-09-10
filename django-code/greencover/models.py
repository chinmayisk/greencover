from django.db import models

class Tree(models.Model):
	x = models.DecimalField(max_digits = 15, decimal_places = 10)
	y = models.DecimalField(max_digits = 15, decimal_places = 10)
	date = models.DateField()
	state = models.IntegerField()
	color = models.CharField(max_length = 100)
	name = models.CharField(max_length = 100)
	comments = models.CharField(max_length = 4096)

	def __unicode__(self):
		tree = '%s (%s, %s)' % (self.name, self.x, self.y)
		return tree

class Achievement(models.Model):
	name = models.CharField(max_length = 400)
	number = models.IntegerField()
	completed = models.CharField(max_length = 1024)

	def __unicode__(self):
		achievements = '%s completed by %s people' %(self.name, self.number)
		return achievements