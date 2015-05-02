import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'heusler_site.settings')


import django
django.setup()
# make sure to put All Inverse Heuslers file in web directory

from heuslers.models import Material

def populate():
	with open("InverseHeuslersDB.csv","r") as myFile:
		tag_number = 1
		for line in myFile:
			line = line.rstrip()
			line = line.split(",")
			
			
			name = line[0]
			Aelement = line[2]
			Belement = line[3]
			Celement = line[4]
			valenceNumber = int(line[1])
			ident = name + "_Xa" 
			structure = "Xa"
			
			magneticMoment = float(line[6])
			latticeConstant = float(line[7])
			
			# Determine if the compound is stable using the formation energy
			
			formationEnergy = line[8]
			if(formationEnergy != "null"):
				formationEnergy = float(formationEnergy)
				if (formationEnergy < 0):
					stable = True
				else:
					stable = False
				
			
			
			polarization = float(line[9])
			
			print("tag_number: " + str(tag_number) + " ident: " + ident + " name: " + name + " Aelement: " + Aelement + " Belement: " + Belement + " Celement: " + Celement + " valenceNumber: " + str(valenceNumber) + " structure: " + structure + " magneticMoment: " + str(magneticMoment) + " latticeConstant: " + str(latticeConstant) + " formationEnergy: " + str(formationEnergy) + " polarization: " + str(polarization) + " stable: " + str(stable))
			
			add_mat(tag_number=tag_number, ident=ident, name=name, Aelement=Aelement, Belement=Belement, Celement=Celement, valenceNumber=valenceNumber, structure=structure, magneticMoment=magneticMoment, latticeConstant=latticeConstant, formationEnergy=formationEnergy, polarization=polarization, stable=stable)
			tag_number = tag_number + 1
			
def add_mat(tag_number, ident, name, Aelement, Belement, Celement, valenceNumber, structure, magneticMoment, latticeConstant, formationEnergy, polarization, stable ):
	m = Material.objects.get_or_create(tag_number=tag_number, ident=ident, name=name, Aelement=Aelement, Belement=Belement, Celement=Celement, valenceNumber=valenceNumber, structure=structure, magneticMoment=magneticMoment, latticeConstant=latticeConstant, formationEnergy=formationEnergy, polarization=polarization, stable=stable)[0]
	return m
	
if __name__ == '__main__':
	print "Starting material test population script ..."
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'heusler_site.settings')
	from heuslers.models import Material
	populate()
