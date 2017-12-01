from django.conf import settings
from django.utils.translation import ugettext as _

from django.core.urlresolvers import reverse

from django.shortcuts import render, get_object_or_404, redirect


from django.contrib import messages
from django.contrib.auth.decorators import login_required




from .models import Telephone, TelephoneAccessoire, Tablette, TabletteAccessoire

from .forms import TelephoneForm, TelephoneAccessoireForm, TabletteForm, TabletteAccessoireForm

# Create your views here.



def create_tel(request):

	form = TelephoneForm(request.POST or None, request.FILES or None)

	if form.is_valid():

		instance = form.save(commit=False)

		instance.save()

		messages.success(request, _("Ce téléphone a été ajouté avec succès"))

		return redirect(reverse("home"))


	context = {
	   "form": form,
	}


	return render(request, "phone/create_tel.html", context)


def phones(request):

	instance = Telephone.objects.all()

	context = {
	  "instance":instance,
	}

	return render(request, "phone/phones.html", context)
