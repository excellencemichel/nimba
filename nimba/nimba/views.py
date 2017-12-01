from django.shortcuts import render

from phone.models import Telephone
from electromenager.models import Frigo, Climatiseur, Ventilateur, Lave_linge, Four


def home(request):


	instance_telephone = Telephone.objects.all()
	instance_frigo = Frigo.objects.all()
	instance_climatiseur = Climatiseur.objects.all()
	instance_ventilateur = Ventilateur.objects.all()
	instance_lave_linge = Lave_linge.objects.all()
	instance_four = Four.objects.all()

	context = {
	    "instance_telephone": instance_telephone,
	    "instance_frigo": instance_frigo,
	    "instance_climatiseur": instance_climatiseur,
	    "instance_ventilateur": instance_ventilateur,
	    "instance_lave_linge": instance_lave_linge,
	    "instance_four" : instance_four,
	}
	return render(request, "home.html", context)