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



class Frigo(models.Model):
	name = models.CharField(max_length=250)
	slug = models.SlugField()
	marque = models.CharField(max_length=250)
	model_frigo = models.CharField(max_length=250)

	prix = models.CharField(max_length=250)
	unite = models.CharField(max_length=250)


	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	photo = models.FileField(upload_to=uplaod_location)



	def __str__(self):
		return self.name




class Climatiseur(models.Model):
	name = models.CharField(max_length=250)
	slug = models.SlugField()
	marque = models.CharField(max_length=250)
	model_climatiseur = models.CharField(max_length=250)

	prix = models.CharField(max_length=250)
	unite = models.CharField(max_length=250)


	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	photo = models.FileField(upload_to=uplaod_location)


	def __str__(self):
		return self.name


class Ventilateur(models.Model):
	name = models.CharField(max_length=250)
	slug = models.SlugField()
	marque = models.CharField(max_length=250)
	model_ventilateur = models.CharField(max_length=250)

	prix = models.CharField(max_length=250)
	unite = models.CharField(max_length=250)


	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	photo = models.FileField(upload_to=uplaod_location)


	def __str__(self):
		return self.name



class Lave_linge(models.Model):
	name = models.CharField(max_length=250)
	slug = models.SlugField()
	marque = models.CharField(max_length=250)
	model_lave_linge = models.CharField(max_length=250)

	prix = models.CharField(max_length=250)
	unite = models.CharField(max_length=250)


	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	photo = models.FileField(upload_to=uplaod_location)



	def __str__(self):
		return self.name


class Four(models.Model):
	name = models.CharField(max_length=250)
	slug = models.SlugField()
	marque = models.CharField(max_length=250)
	model_four = models.CharField(max_length=250)

	prix = models.CharField(max_length=250)
	unite = models.CharField(max_length=250)


	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	photo = models.FileField(upload_to=uplaod_location)


	def __str__(self):
		return self.name





def create_slug_frigo(instance, new_slug=None):
	slug = slugify(instance.name)
	if new_slug is not None:
		slug = new_slug

	qs = Frigo.objects.filter(slug=slug).order_by("-id")
	exists = qs.exists()

	if exists:
		new_slug = "%s-%s" %(slug, qs.first().id)
		return create_slug_frigo(instance, new_slug=new_slug)
	return slug


def pre_save_post_receiver_frigo(sender, instance, *args, **kwargs):
	if not instance.slug or instance.slug != instance.name:
		instance.slug = create_slug_frigo(instance)



def create_slug_climatiseur(instance, new_slug=None):
	slug = slugify(instance.name)
	if new_slug is not None:
		slug = new_slug

	qs = Climatiseur.objects.filter(slug=slug).order_by("-id")
	exists = qs.exists()

	if exists:
		new_slug = "%s-%s" %(slug, qs.first().id)
		return create_slug_climatiseur(instance, new_slug=new_slug)
	return slug


def pre_save_post_receiver_climatiseur(sender, instance, *args, **kwargs):
	if not instance.slug or instance.slug != instance.name:
		instance.slug = create_slug_climatiseur(instance)



def create_slug_ventilateur(instance, new_slug=None):
	slug = slugify(instance.name)
	if new_slug is not None:
		slug = new_slug

	qs = Ventilateur.objects.filter(slug=slug).order_by("-id")
	exists = qs.exists()

	if exists:
		new_slug = "%s-%s" %(slug, qs.first().id)
		return create_slug_ventilateur(instance, new_slug=new_slug)
	return slug


def pre_save_post_receiver_ventilateur(sender, instance, *args, **kwargs):
	if not instance.slug or instance.slug != instance.name:
		instance.slug = create_slug_ventilateur(instance)



def create_slug_lave_linge(instance, new_slug=None):
	slug = slugify(instance.name)
	if new_slug is not None:
		slug = new_slug

	qs = Lave_linge.objects.filter(slug=slug).order_by("-id")
	exists = qs.exists()

	if exists:
		new_slug = "%s-%s" %(slug, qs.first().id)
		return create_slug_lave_linge(instance, new_slug=new_slug)
	return slug


def pre_save_post_receiver_lave_linge(sender, instance, *args, **kwargs):
	if not instance.slug or instance.slug != instance.name:
		instance.slug = create_slug_lave_linge(instance)



def create_slug_four(instance, new_slug=None):
	slug = slugify(instance.name)
	if new_slug is not None:
		slug = new_slug

	qs = Frigo.objects.filter(slug=slug).order_by("-id")
	exists = qs.exists()

	if exists:
		new_slug = "%s-%s" %(slug, qs.first().id)
		return create_slug_four(instance, new_slug=new_slug)
	return slug


def pre_save_post_receiver_four(sender, instance, *args, **kwargs):
	if not instance.slug or instance.slug != instance.name:
		instance.slug = create_slug_four(instance)









pre_save.connect(pre_save_post_receiver_frigo, sender=Frigo)

pre_save.connect(pre_save_post_receiver_climatiseur, sender=Climatiseur)

pre_save.connect(pre_save_post_receiver_ventilateur, sender=Ventilateur)

pre_save.connect(pre_save_post_receiver_lave_linge, sender=Lave_linge)

pre_save.connect(pre_save_post_receiver_four, sender=Four)


