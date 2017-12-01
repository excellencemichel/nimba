from time import strftime
from random import randrange
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import pre_save

from django.utils.text import slugify


# Create your models here.



def uplaod_location(instance, filename):
	extension = filename.split(".")[-1]
	jour = strftime("%a")
	temps = strftime("%d-%m-%Y-%H-%M-%S")
	pseudo = randrange(-1000000,1000000)
	print(extension)
	return "{}/{}_{}.{}".format(jour, temps, pseudo, extension)


class Telephone(models.Model):
	name = models.CharField(max_length=250)
	slug = models.SlugField()
	marque = models.CharField(max_length=250)
	model_tel = models.CharField(max_length=250)

	prix = models.CharField(max_length=250)
	unite = models.CharField(max_length=250)

	description = models.TextField(null=True, blank=True)


	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	photo = models.FileField(upload_to=uplaod_location)


	categorie_telephone = models.CharField(max_length=250)


class TelephoneAccessoire(models.Model):
	name = models.CharField(max_length=250)
	slug = models.SlugField()
	marque = models.CharField(max_length=250)
	model_tel = models.CharField(max_length=250)

	prix = models.CharField(max_length=250)
	unite = models.CharField(max_length=250)


	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	photo = models.FileField(upload_to=uplaod_location)




class Tablette(models.Model):
	name = models.CharField(max_length=250)
	slug = models.SlugField()
	marque = models.CharField(max_length=250)
	model_tab = models.CharField(max_length=250)

	prix = models.CharField(max_length=250)
	unite = models.CharField(max_length=250)


	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	photo = models.FileField(upload_to=uplaod_location)


	categorie_tablette = models.CharField(max_length=250)




	def __str__(self):
		return self.name


class TabletteAccessoire(models.Model):
	name = models.CharField(max_length=250)
	slug = models.SlugField()
	marque = models.CharField(max_length=250)
	model_tab = models.CharField(max_length=250)

	prix = models.CharField(max_length=250)
	unite = models.CharField(max_length=250)


	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	photo = models.FileField(upload_to=uplaod_location)





########################## Slug pour les téléphones #####################################

def create_slug_tel(instance, new_slug=None):
	slug = slugify(instance.name)
	if new_slug is not None:
		slug = new_slug

	qs = Telephone.objects.filter(slug=slug).order_by("-id")
	exists = qs.exists()

	if exists:
		new_slug = "%s-%s" %(slug, qs.first().id)
		return create_slug_tel(instance, new_slug=new_slug)
	return slug


def pre_save_post_receiver_tel(sender, instance, *args, **kwargs):
	if not instance.slug or instance.slug != instance.name:
		instance.slug = create_slug_tel(instance)


########################## Slug pour les téléphones accessoires #########################

def create_slug_tel_acc(instance, new_slug=None):
	slug = slugify(instance.name)
	if new_slug is not None:
		slug = new_slug

	qs = Telephone.objects.filter(slug=slug).order_by("-id")
	exists = qs.exists()

	if exists:
		new_slug = "%s-%s" %(slug, qs.first().id)
		return create_slug_tel_acc(instance, new_slug=new_slug)
	return slug


def pre_save_post_receiver_tel_acc(sender, instance, *args, **kwargs):
	if not instance.slug or instance.slug != instance.name:
		instance.slug = create_slug_tel_acc(instance)



########################## Slug pour les tablettes #####################################

def create_slug_tab(instance, new_slug=None):
	slug = slugify(instance.name)
	if new_slug is not None:
		slug = new_slug

	qs = Telephone.objects.filter(slug=slug).order_by("-id")
	exists = qs.exists()

	if exists:
		new_slug = "%s-%s" %(slug, qs.first().id)
		return create_slug_tab(instance, new_slug=new_slug)
	return slug


def pre_save_post_receiver_tab(sender, instance, *args, **kwargs):
	if not instance.slug or instance.slug != instance.name:
		instance.slug = create_slug_tab(instance)



########################## Slug pour les tablettes accessoires #####################################


def create_slug_tab_acc(instance, new_slug=None):
	slug = slugify(instance.name)
	if new_slug is not None:
		slug = new_slug

	qs = Telephone.objects.filter(slug=slug).order_by("-id")
	exists = qs.exists()

	if exists:
		new_slug = "%s-%s" %(slug, qs.first().id)
		return create_slug_tab_acc(instance, new_slug=new_slug)
	return slug


def pre_save_post_receiver_tab_acc(sender, instance, *args, **kwargs):
	if not instance.slug or instance.slug != instance.name:
		instance.slug = create_slug_tab_acc(instance)



pre_save.connect(pre_save_post_receiver_tel, sender=Telephone)
pre_save.connect(pre_save_post_receiver_tel_acc, sender=TelephoneAccessoire)
pre_save.connect(pre_save_post_receiver_tab, sender=Tablette)
pre_save.connect(pre_save_post_receiver_tab_acc, sender=TabletteAccessoire)



