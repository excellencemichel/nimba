from django.contrib import admin

from .models import Frigo, Climatiseur, Ventilateur, Lave_linge, Four

# Register your models here.



class FrigoAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug":("name",),}



class ClimatiseurAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug":("name",),}



class VentilateurAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug":("name",),}



class Lave_lingeAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug":("name",),}



class FourAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug":("name",),}



admin.site.register(Frigo, FrigoAdmin)
admin.site.register(Climatiseur, ClimatiseurAdmin)
admin.site.register(Ventilateur, VentilateurAdmin)
admin.site.register(Lave_linge, Lave_lingeAdmin)
admin.site.register(Four, FourAdmin)

