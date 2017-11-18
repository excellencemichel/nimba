from django.db import models
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

class Samsung(models.Model):
	name = models.CharField(max_length=250)
	slug = models.SlugField()
	marque = models.CharField(max_length=250)
	modelp = models.CharField(max_length=250)

	prix = models.CharField(max_length=250)
	unite = models.CharField(max_length=250)


	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	photo = models.FileField(upload_to=uplaod_location)

def create_slug_samsung(instance, new_slug=None):
	slug = slugify(instance.name)
	if new_slug is not None:
		slug = new_slug

	qs = Samsung.objects.filter(slug=slug).order_by("-id")
	exists = qs.exists()

	if exists:
		new_slug = "%s-%s" %(slug, qs.first().id)
		return create_slug_samsung(instance, new_slug=new_slug)
	return slug


def pre_save_post_receiver_samsung(sender, instance, *args, **kwargs):
	if not instance.slug or instance.slug != instance.name:
		instance.slug = create_slug_samsung(instance)




class Iphone(models.Model):
	name = models.CharField(max_length=250)
	slug = models.SlugField()
	marque = models.CharField(max_length=250)
	modelp = models.CharField(max_length=250)

	prix = models.CharField(max_length=250)
	unite = models.CharField(max_length=250)


	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	photo = models.FileField(upload_to=uplaod_location)


def create_slug_iphone(instance, new_slug=None):
	slug = slugify(instance.name)
	if new_slug is not None:
		slug = new_slug

	qs = Iphone.objects.filter(slug=slug).order_by("-id")
	exists = qs.exists()

	if exists:
		new_slug = "%s-%s" %(slug, qs.first().id)
		return create_slug_iphone(instance, new_slug=new_slug)
	return slug


def pre_save_post_receiver_iphone(sender, instance, *args, **kwargs):
	if not instance.slug or instance.slug != instance.name:
		instance.slug = create_slug_iphone(instance)




class Infinix(models.Model):
	name = models.CharField(max_length=250)
	slug = models.SlugField()
	marque = models.CharField(max_length=250)
	modelp = models.CharField(max_length=250)

	prix = models.CharField(max_length=250)
	unite = models.CharField(max_length=250)


	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	photo = models.FileField(upload_to=uplaod_location)



def create_slug_infinix(instance, new_slug=None):
	slug = slugify(instance.name)
	if new_slug is not None:
		slug = new_slug

	qs = Infinix.objects.filter(slug=slug).order_by("-id")
	exists = qs.exists()

	if exists:
		new_slug = "%s-%s" %(slug, qs.first().id)
		return create_slug_infinix(instance, new_slug=new_slug)
	return slug


def pre_save_post_receiver_infinix(sender, instance, *args, **kwargs):
	if not instance.slug or instance.slug != instance.name:
		instance.slug = create_slug_infinix(instance)




class Wiko(models.Model):
	name = models.CharField(max_length=250)
	slug = models.SlugField()
	marque = models.CharField(max_length=250)
	modelp = models.CharField(max_length=250)

	prix = models.CharField(max_length=250)
	unite = models.CharField(max_length=250)


	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	photo = models.FileField(upload_to=uplaod_location)



def create_slug_wiko(instance, new_slug=None):
	slug = slugify(instance.name)
	if new_slug is not None:
		slug = new_slug

	qs = Wiko.objects.filter(slug=slug).order_by("-id")
	exists = qs.exists()

	if exists:
		new_slug = "%s-%s" %(slug, qs.first().id)
		return create_slug_wiko(instance, new_slug=new_slug)
	return slug


def pre_save_post_receiver_wiko(sender, instance, *args, **kwargs):
	if not instance.slug or instance.slug != instance.name:
		instance.slug = create_slug_wiko(instance)




class Accent(models.Model):
	name = models.CharField(max_length=250)
	slug = models.SlugField()
	marque = models.CharField(max_length=250)
	modelp = models.CharField(max_length=250)

	prix = models.CharField(max_length=250)
	unite = models.CharField(max_length=250)


	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	photo = models.FileField(upload_to=uplaod_location)



def create_slug_accent(instance, new_slug=None):
	slug = slugify(instance.name)
	if new_slug is not None:
		slug = new_slug

	qs = Accent.objects.filter(slug=slug).order_by("-id")
	exists = qs.exists()

	if exists:
		new_slug = "%s-%s" %(slug, qs.first().id)
		return create_slug_accent(instance, new_slug=new_slug)
	return slug


def pre_save_post_receiver_accent(sender, instance, *args, **kwargs):
	if not instance.slug or instance.slug != instance.name:
		instance.slug = create_slug_accent(instance)




class Huawai(models.Model):
	name = models.CharField(max_length=250)
	slug = models.SlugField()
	marque = models.CharField(max_length=250)
	modelp = models.CharField(max_length=250)

	prix = models.CharField(max_length=250)
	unite = models.CharField(max_length=250)


	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	photo = models.FileField(upload_to=uplaod_location)



def create_slug_huawai(instance, new_slug=None):
	slug = slugify(instance.name)
	if new_slug is not None:
		slug = new_slug

	qs = Huawai.objects.filter(slug=slug).order_by("-id")
	exists = qs.exists()

	if exists:
		new_slug = "%s-%s" %(slug, qs.first().id)
		return create_slug_huawai(instance, new_slug=new_slug)
	return slug


def pre_save_post_receiver_huawai(sender, instance, *args, **kwargs):
	if not instance.slug or instance.slug != instance.name:
		instance.slug = create_slug_huawai(instance)




class Blackbery(models.Model):
	name = models.CharField(max_length=250)
	slug = models.SlugField()
	marque = models.CharField(max_length=250)
	modelp = models.CharField(max_length=250)

	prix = models.CharField(max_length=250)
	unite = models.CharField(max_length=250)


	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	photo = models.FileField(upload_to=uplaod_location)



def create_slug_blackbery(instance, new_slug=None):
	slug = slugify(instance.name)
	if new_slug is not None:
		slug = new_slug

	qs = Blackbery.objects.filter(slug=slug).order_by("-id")
	exists = qs.exists()

	if exists:
		new_slug = "%s-%s" %(slug, qs.first().id)
		return create_slug_blackbery(instance, new_slug=new_slug)
	return slug


def pre_save_post_receiver_blackbery(sender, instance, *args, **kwargs):
	if not instance.slug or instance.slug != instance.name:
		instance.slug = create_slug_blackbery(instance)




class Tecno(models.Model):
	name = models.CharField(max_length=250)
	slug = models.SlugField()
	marque = models.CharField(max_length=250)
	modelp = models.CharField(max_length=250)

	prix = models.CharField(max_length=250)
	unite = models.CharField(max_length=250)


	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	photo = models.FileField(upload_to=uplaod_location)


def create_slug_tecno(instance, new_slug=None):
	slug = slugify(instance.name)
	if new_slug is not None:
		slug = new_slug

	qs = Tecno.objects.filter(slug=slug).order_by("-id")
	exists = qs.exists()

	if exists:
		new_slug = "%s-%s" %(slug, qs.first().id)
		return create_slug_tecno(instance, new_slug=new_slug)
	return slug


def pre_save_post_receiver_tecno(sender, instance, *args, **kwargs):
	if not instance.slug or instance.slug != instance.name:
		instance.slug = create_slug_tecno(instance)



class Motorola(models.Model):
	name = models.CharField(max_length=250)
	slug = models.SlugField()
	marque = models.CharField(max_length=250)
	modelp = models.CharField(max_length=250)

	prix = models.CharField(max_length=250)
	unite = models.CharField(max_length=250)


	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	photo = models.FileField(upload_to=uplaod_location)


def create_slug_motorola(instance, new_slug=None):
	slug = slugify(instance.name)
	if new_slug is not None:
		slug = new_slug

	qs = Motorola.objects.filter(slug=slug).order_by("-id")
	exists = qs.exists()

	if exists:
		new_slug = "%s-%s" %(slug, qs.first().id)
		return create_slug_motorola(instance, new_slug=new_slug)
	return slug


def pre_save_post_receiver_motorala(sender, instance, *args, **kwargs):
	if not instance.slug or instance.slug != instance.name:
		instance.slug = create_slug_motorola(instance)




class Lenovo(models.Model):
	name = models.CharField(max_length=250)
	slug = models.SlugField()
	marque = models.CharField(max_length=250)
	modelp = models.CharField(max_length=250)

	prix = models.CharField(max_length=250)
	unite = models.CharField(max_length=250)


	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	photo = models.FileField(upload_to=uplaod_location)



def create_slug_lenovo(instance, new_slug=None):
	slug = slugify(instance.name)
	if new_slug is not None:
		slug = new_slug

	qs = Lenovo.objects.filter(slug=slug).order_by("-id")
	exists = qs.exists()

	if exists:
		new_slug = "%s-%s" %(slug, qs.first().id)
		return create_slug_lenovo(instance, new_slug=new_slug)
	return slug


def pre_save_post_receiver_lenovo(sender, instance, *args, **kwargs):
	if not instance.slug or instance.slug != instance.name:
		instance.slug = create_slug_lenovo(instance)





class Sony(models.Model):
	name = models.CharField(max_length=250)
	slug = models.SlugField()
	marque = models.CharField(max_length=250)
	modelp = models.CharField(max_length=250)

	prix = models.CharField(max_length=250)
	unite = models.CharField(max_length=250)


	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	photo = models.FileField(upload_to=uplaod_location)


def create_slug_sony(instance, new_slug=None):
	slug = slugify(instance.name)
	if new_slug is not None:
		slug = new_slug

	qs = Sony.objects.filter(slug=slug).order_by("-id")
	exists = qs.exists()

	if exists:
		new_slug = "%s-%s" %(slug, qs.first().id)
		return create_slug_sony(instance, new_slug=new_slug)
	return slug


def pre_save_post_receiver_sony(sender, instance, *args, **kwargs):
	if not instance.slug or instance.slug != instance.name:
		instance.slug = create_slug_sony(instance)



class Oppo(models.Model):
	name = models.CharField(max_length=250)
	slug = models.SlugField()
	marque = models.CharField(max_length=250)
	modelp = models.CharField(max_length=250)

	prix = models.CharField(max_length=250)
	unite = models.CharField(max_length=250)


	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	photo = models.FileField(upload_to=uplaod_location)



def create_slug_oppo(instance, new_slug=None):
	slug = slugify(instance.name)
	if new_slug is not None:
		slug = new_slug

	qs = Oppo.objects.filter(slug=slug).order_by("-id")
	exists = qs.exists()

	if exists:
		new_slug = "%s-%s" %(slug, qs.first().id)
		return create_slug_oppo(instance, new_slug=new_slug)
	return slug


def pre_save_post_receiver_oppo(sender, instance, *args, **kwargs):
	if not instance.slug or instance.slug != instance.name:
		instance.slug = create_slug_oppo(instance)




class Nokia(models.Model):
	name = models.CharField(max_length=250)
	slug = models.SlugField()
	marque = models.CharField(max_length=250)
	modelp = models.CharField(max_length=250)

	prix = models.CharField(max_length=250)
	unite = models.CharField(max_length=250)


	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	photo = models.FileField(upload_to=uplaod_location)


def create_slug_nokia(instance, new_slug=None):
	slug = slugify(instance.name)
	if new_slug is not None:
		slug = new_slug

	qs = Nokia.objects.filter(slug=slug).order_by("-id")
	exists = qs.exists()

	if exists:
		new_slug = "%s-%s" %(slug, qs.first().id)
		return create_slug_nokia(instance, new_slug=new_slug)
	return slug


def pre_save_post_receiver_nokia(sender, instance, *args, **kwargs):
	if not instance.slug or instance.slug != instance.name:
		instance.slug = create_slug_nokia(instance)




class Itel(models.Model):
	name = models.CharField(max_length=250)
	slug = models.SlugField()
	marque = models.CharField(max_length=250)
	modelp = models.CharField(max_length=250)

	prix = models.CharField(max_length=250)
	unite = models.CharField(max_length=250)


	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	photo = models.FileField(upload_to=uplaod_location)




def create_slug_itel(instance, new_slug=None):
	slug = slugify(instance.name)
	if new_slug is not None:
		slug = new_slug

	qs = Itel.objects.filter(slug=slug).order_by("-id")
	exists = qs.exists()

	if exists:
		new_slug = "%s-%s" %(slug, qs.first().id)
		return create_slug_itel(instance, new_slug=new_slug)
	return slug


def pre_save_post_receiver_itel(sender, instance, *args, **kwargs):
	if not instance.slug or instance.slug != instance.name:
		instance.slug = create_slug_itel(instance)






pre_save.connect(pre_save_post_receiver_samsung, sender=Samsung)
pre_save.connect(pre_save_post_receiver_iphone, sender=Iphone)
pre_save.connect(pre_save_post_receiver_infinix, sender=Infinix)
pre_save.connect(pre_save_post_receiver_accent, sender=Accent)
pre_save.connect(pre_save_post_receiver_wiko, sender=Wiko)
pre_save.connect(pre_save_post_receiver_huawai, sender=Huawai)
pre_save.connect(pre_save_post_receiver_blackbery, sender=Blackbery)
pre_save.connect(pre_save_post_receiver_sony, sender=Sony)
pre_save.connect(pre_save_post_receiver_tecno, sender=Tecno)
pre_save.connect(pre_save_post_receiver_itel, sender=Itel)
pre_save.connect(pre_save_post_receiver_lenovo, sender=Lenovo)
pre_save.connect(pre_save_post_receiver_nokia, sender=Nokia)
pre_save.connect(pre_save_post_receiver_oppo, sender=Oppo)
pre_save.connect(pre_save_post_receiver_motorala, sender=Motorola)


