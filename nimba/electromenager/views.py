from django.conf import settings
from django.utils.translation import ugettext as _

from django.core.urlresolvers import reverse

from django.shortcuts import render, get_object_or_404, redirect


from django.contrib import messages
from django.contrib.auth.decorators import login_required


from .forms import FrigoForm, ClimatiseurForm, VentilateurForm, Lave_lingeForm, FourForm


# Create your views here.




def create_frigo(request):

	form = FrigoForm(request.POST or None, request.FILES or None)

	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, _("Ce frigo a été ajouté avec succès"))
		return redirect(reverse("home"))



	context = {
	   "form" : form,
	}

	return render(request, "electromenager/create_frigo.html", context)



def create_climatiseur(request):

	form = ClimatiseurForm(request.POST or None, request.FILES or None)

	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()

		messages.success(request, _("Ce climatiseur a été ajouté avec succès"))
		return redirect(reverse("home"))



	context = {
	   "form" : form,
	}

	return render(request, "electromenager/create_climatiseur.html", context)





def create_ventilateur(request):

	form = VentilateurForm(request.POST or None, request.FILES or None)

	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()

		messages.success(request, _("Ce ventilateur a été ajouté avec succès"))
		return redirect(reverse("home"))



	context = {
	   "form" : form,
	}

	return render(request, "electromenager/create_ventilateur.html", context)




def create_lave_linge(request):

	form = Lave_lingeForm(request.POST or None, request.FILES or None)

	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()

		messages.success(request, _("Ce Lave linge a été ajouté avec succès"))
		return redirect(reverse("home"))



	context = {
	   "form" : form,
	}

	return render(request, "electromenager/create_lave_linge.html", context)



def create_four(request):

	form = FourForm(request.POST or None, request.FILES or None)

	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()

		messages.success(request, _("Ce four a été ajouté avec succès"))
		return redirect(reverse("home"))



	context = {
	   "form" : form,
	}

	return render(request, "electromenager/create_four.html", context)