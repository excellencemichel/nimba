from django.conf.urls import url



from .views import ( create_frigo, create_climatiseur,
                create_ventilateur, create_lave_linge, 
                 create_four)



urlpatterns = [
           url(r'^create-frigo/$', create_frigo, name="create_frigo"),
           url(r'^create-climatiseur/$', create_climatiseur, name="create_climatiseur"),
           url(r'^create-ventilateur/$', create_ventilateur, name="create_ventilateur"),
           url(r'^create-lave-linge/$', create_lave_linge, name="create_lave_linge"),
           url(r'^create-four/$', create_four, name="create_four"),



           

  ]