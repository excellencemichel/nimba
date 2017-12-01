from django.contrib import admin

from .models import Telephone, TelephoneAccessoire,  Tablette, TabletteAccessoire
# Register your models here.



class TelephoneAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug":("name",),}


class TelephoneAccessoireAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug":("name",),}



class TabletteAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug":("name",),}



class TabletteAccessoireAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug":("name",),}


admin.site.register(Telephone, TelephoneAdmin)
admin.site.register(TelephoneAccessoire, TelephoneAccessoireAdmin)
admin.site.register(Tablette, TabletteAdmin)
admin.site.register(TabletteAccessoire, TabletteAccessoireAdmin)


