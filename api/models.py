from django.db import models

class Repositories(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=256, verbose_name="name")
	url = models.CharField(max_length=1024, verbose_name="URL")


class Packages(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=256, verbose_name="name")


class Users(models.Model):
	id = models.AutoField(primary_key=True)
	username = models.Field(max_length=100,verbose_name="username")
	fullname = models.CharField(max_length=100,verbose_name="fullname")
	email = models.CharField(max_length=256,verbose_name="email")
	repositories = models.ManyToManyField(Repositories,verbose_name="repositories")
	packages = models.ManyToManyField(Packages,verbose_name="packages")

	class Meta:
		verbose_name = "User"
		verbose_name_plural = "Users"

	def __str__(self):
		return "%s" % (self.username)