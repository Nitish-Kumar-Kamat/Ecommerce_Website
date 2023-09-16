from django.db import models

class CustomManager(models.Manager):
	def get_product(self,p1,p2):
		return super().get_queryset().filter(price__range=(p1,p2))