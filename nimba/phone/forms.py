from django.utils.translation import ugettext_lazy as _
from django import forms

from .models import Telephone, TelephoneAccessoire, Tablette, TabletteAccessoire 


class TelephoneForm(forms.ModelForm):

	CATEGORIE = (
         ("Samsung", "Samsung"),
         ("Iphone", "Iphone"),
         ("Oppo", "Oppo"),
         ("Infinix", "Infinix"),
         ("Nokia", "Nokia"),
         ("Tecno", "Tecno"),
         ("Lenovo", "Lenovo"),
         ("Wiko", "Wiko"),
         ("Huawai", "Huawai"),
         ("Blackbery", "Blackbery"),
         ("Itel", "Itel"),


     
		)


	name = forms.CharField(label=_("Nom du téléphone"))
	marque = forms.CharField(label=_("Marque"))
	model_tel = forms.CharField(label=_("Model"))
	photo = forms.FileField(label=_("Photos"))
	categorie_telephone = forms.ChoiceField(label=_("Catégorie de téléphone"), choices=CATEGORIE)


	class Meta:
		model = Telephone
		fields = ("categorie_telephone" ,"name", "marque","model_tel", "prix", "unite", "photo", "description",)





class TelephoneAccessoireForm(forms.ModelForm):


	name = forms.CharField(label=_("Nom du téléphone"))
	marque = forms.CharField(label=_("Marque"))
	model_tel = forms.CharField(label=_("Model"))
	photo = forms.FileField(label=_("Photos"))


	class Meta:
		model = TelephoneAccessoire
		fields = ( "name", "marque","model_tel", "photo",)




class TabletteForm(forms.ModelForm):

	CATEGORIE = (
         ("Samsung", "Samsung"),
         ("Iphone", "Iphone"),
         ("Oppo", "Oppo"),
         ("Infinix", "Infinix"),
         ("Nokia", "Nokia"),
         ("Tecno", "Tecno"),
         ("Lenovo", "Lenovo"),
         ("Wiko", "Wiko"),
         ("Huawai", "Huawai"),
         ("Blackbery", "Blackbery"),
         ("Itel", "Itel"),


     
		)


	name = forms.CharField(label=_("Nom du téléphone"))
	marque = forms.CharField(label=_("Marque"))
	model_tel = forms.CharField(label=_("Model"))
	photo = forms.CharField(label=_("Photos"))

	categorie_tablette = forms.ChoiceField(label=_("La catégorie de la tablette"), choices=CATEGORIE)


	class Meta:
		model = Tablette
		fields = ("categorie_tablette", "name", "marque","model_tel", "photo",)



class TabletteAccessoireForm(forms.ModelForm):


	name = forms.CharField(label=_("Nom du téléphone"))
	marque = forms.CharField(label=_("Marque"))
	model_tel = forms.CharField(label=_("Model"))
	photo = forms.CharField(label=_("Photos"))


	class Meta:
		model = TabletteAccessoire
		fields = ( "name", "marque","model_tel", "photo",)
