from django.db import models

# Create your models here.
class Material(models.Model):
	
	tag_number = models.IntegerField(unique=True)
	ident = models.CharField(max_length=128, unique=True)	# Sc2TiAl-L21
	name = models.CharField(max_length=128)				# Sc2TiAl
	Aelement = models.CharField(max_length=2)
	Belement = models.CharField(max_length=2)
	Celement = models.CharField(max_length=2)
	valenceNumber = models.IntegerField()
	structure = models.CharField(max_length=4)
	
	magneticMoment = models.DecimalField(max_digits = 20, decimal_places = 10, null=True, blank=True)
	latticeConstant = models.DecimalField(max_digits = 20, decimal_places = 10, null=True, blank=True)
	formationEnergy = models.DecimalField(max_digits = 20, decimal_places = 10, null=True, blank=True)
	polarization = models.DecimalField(max_digits = 20, decimal_places = 10, null=True, blank=True)
	
	stable = models.NullBooleanField(null=True, blank=True)
	
	
	
	def __unicode__(self):
		return self.id