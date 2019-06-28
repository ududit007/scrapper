from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
	name = models.CharField(max_length=50)
	email = models.EmailField(max_length=100, unique=True)
	password = models.CharField(max_length=128)
	is_active = models.BooleanField(default=True)

	USERNAME_FIELD = 'email'
	objects = UserManager()

	@property
	def is_staff(self):
		return self.is_superuser

	def clean(self):
		if self.email is not None:
			self.email = self.email.lower()

		return super(User, self).clean()

	def __str__(self):
		return '{}'.format(self.name)

	def __repr__(self):
		return '<User: {}>'.format(self.name)

	class Meta:
		db_table = 'user'
		verbose_name = 'User'
		verbose_name_plural = 'Users'


class ScrappedData(models.Model):
	source = models.CharField(max_length=20)
	name = models.CharField(max_length=50)
	actual_price = models.FloatField(default=0)
	selling_price = models.FloatField(default=0)
	rating = models.FloatField(default=1)
	image = models.URLField(null=True, blank=True)

	def __str__(self):
		return '{}'.format(self.name)

	def __repr__(self):
		return '<ScrappedData: {}>'.format(self.name)

	class Meta:
		db_table = 'scrapped_data'
		verbose_name = 'Scrapped_data'
		verbose_name_plural = 'Scrapped_data'
