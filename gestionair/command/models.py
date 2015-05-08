from django.db import models

# Create your models here.

class Participant(models.Model):
   nom = models.CharField(max_length=50)

class Groupe(models.Model):
	libelle = models.CharField(max_length=50)
	status = models.CharField(max_length=30)
