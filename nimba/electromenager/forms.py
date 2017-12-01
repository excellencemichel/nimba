from django.utils.translation import ugettext_lazy as _
from django import forms

from .models import Frigo, Climatiseur, Ventilateur, Lave_linge, Four


class FrigoForm(forms.ModelForm):

	name = forms.CharField(label=_("Nom du refrigérateur"))
	marque = forms.CharField(label=_("Marque"))
	model_frigo = forms.CharField(label=_("Model"))

	prix = forms.CharField(label=_("le prix du refrigérateur"))
	unite = forms.CharField(label=_("L'unité d'évaluaton de prix, $ ou € ou ..."))
	photo = forms.FileField(label=_("Photos"))


	class Meta:
		model = Frigo
		fields = ("name", "marque","model_frigo", "prix", "unite", "photo",)




class ClimatiseurForm(forms.ModelForm):

	name = forms.CharField(label=_("Nom du climatiseur"))
	marque = forms.CharField(label=_("Marque"))
	model_climatiseur = forms.CharField(label=_("Model"))
	prix = forms.CharField(label=_("Le prix du climatiseur"))
	unite = forms.CharField(label=_("L'unité d'évaluaton du prix du climatiseur, $ ou € ou ..."))
	photo = forms.FileField(label=_("Photos"))


	class Meta:
		model = Climatiseur
		fields = ("name", "marque","model_climatiseur", "prix", "unite", "photo",)




class VentilateurForm(forms.ModelForm):

	name = forms.CharField(label=_("Nom du ventilateur"))
	marque = forms.CharField(label=_("Marque"))
	model_ventilateur = forms.CharField(label=_("Model"))
	prix = forms.CharField(label=_("Le prix du ventilateur"))
	unite = forms.CharField(label=_("l'unité d'évaluaton du prix du ventilateur, $ ou € ou ..."))
	photo = forms.FileField(label=_("Photos"))


	class Meta:
		model = Ventilateur
		fields = ("name", "marque","model_ventilateur", "prix", "unite", "photo",)



class Lave_lingeForm(forms.ModelForm):

	name = forms.CharField(label=_("Nom de la machine lave linge"))
	marque = forms.CharField(label=_("Marque"))
	model_lave_linge = forms.CharField(label=_("Model"))
	prix = forms.CharField(label=_("Le prix de la machine"))
	unite = forms.CharField(label=_("L'unité D'évaluaton prix de la machine"))
	photo = forms.FileField(label=_("Photos"))


	class Meta:
		model = Lave_linge
		fields = ("name", "marque","model_lave_linge", "prix", 'unite', "photo",)



class FourForm(forms.ModelForm):

	name = forms.CharField(label=_("Nom du four"))
	marque = forms.CharField(label=_("Marque"))
	model_four = forms.CharField(label=_("Model"))
	prix = forms.CharField(label=_("Le prix du four"))
	unite = forms.CharField(label=_("L'unité d'évaluaton du prix du four"))
	photo = forms.FileField(label=_("Photos"))


	class Meta:
		model = Four
		fields = ("name", "marque","model_four", "prix", "unite", "photo",)