from django.db import models

class MisDatos(models.Model):
	nombre = models.CharField(max_length=30)
	skills = models.TextField()
	telefono = models.IntegerField()
	email = models.EmailField()
	imagen = models.FileField()
	facebook = models.CharField(max_length=30)
	twitter = models.CharField(max_length=30)
	youtube = models.CharField(max_length=30)

	def __unicode__(self):
		return self.nombre