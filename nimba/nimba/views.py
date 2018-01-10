from django.shortcuts import render

from phone.models import Telephone
from electromenager.models import Frigo, Climatiseur, Ventilateur, Lave_linge, Four


def home(request):


	telephone = Telephone.objects.all()
	instance_samsung = telephone.filter(categorie_telephone__icontains="samsung")
	instance_iphone = telephone.filter(categorie_telephone__icontains="iphone")

	instance_frigo = Frigo.objects.all()
	instance_climatiseur = Climatiseur.objects.all()
	instance_ventilateur = Ventilateur.objects.all()
	instance_lave_linge = Lave_linge.objects.all()
	instance_four = Four.objects.all()

	context = {
	    "instance_samsung": instance_samsung,
	    "instance_iphone": instance_iphone,

	    "instance_frigo": instance_frigo,
	    "instance_climatiseur": instance_climatiseur,
	    "instance_ventilateur": instance_ventilateur,
	    "instance_lave_linge": instance_lave_linge,
	    "instance_four" : instance_four,
	}
	return render(request, "home.html", context)



def hand(request):
	return render(request, "hand.html")