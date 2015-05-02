# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render
from heuslers.models import Material
from django.core.mail import send_mail
from .forms import ContactForm
#from django.utils import simplejson

def about(request):
	context_dict = {}
	return render(request, 'heuslers/about.html', context_dict)

def home(request):
	context_dict = {}
	return render(request, 'heuslers/home.html', context_dict)
	
def thanks(request):
	context_dict = {}
	return render(request, 'heuslers/thanks.html', context_dict)

def index(request):
	material_list = Material.objects.order_by('tag_number')
	#context_dict = {'materials': material_list, 'js_data': '{{"name": "Co2FeSi"}}'}

	js_materials = '['
	for material in material_list:
		material.url = material.name
		js_materials = js_materials + '{ "name":"' + material.name + '", "ident": "' + material.ident + '", "formationEnergy": "' + str(material.formationEnergy) + '", "magneticMoment": "' + str(material.magneticMoment)  + '", "Aelement": "' + material.Aelement + '", "Belement": "' + material.Belement + '","Celement": "'+ material.Celement + '","structure": "' + material.structure + '","stable": "' + str(material.stable) + '"},'
	js_materials = js_materials[:-1] + ']' #the -1 part gets rid of last comma
	context_dict = {'js_data': js_materials}
	return render(request, 'heuslers/index.html', context_dict)
	
def material(request, material_name_url):
	
	context_dict = {}
	
	try:
		material = Material.objects.get(ident=material_name_url)
		
		context_dict['material'] = material
	except Material.DoesNotExist:
		pass
	
	return render(request, 'heuslers/material.html', context_dict)

def contact(request):
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = form.cleaned_data['subject']
			message = form.cleaned_data['message']
			sender = form.cleaned_data['sender']
			cc_myself = form.cleaned_data['cc_myself']
			
			message = "Contact request from " + sender + "\n" +message 
			
			recipients = ['clample@crimson.ua.edu']
			if cc_myself:
				recipients.append(sender)
			
			send_mail(subject, message, sender, recipients)
			return HttpResponseRedirect('/heuslers/thanks/')
	# if a GET, we'll create a blank form
	else:
		form = ContactForm()
	return render(request, 'heuslers/contact.html', {'form': form})