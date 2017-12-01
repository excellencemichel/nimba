from django.conf.urls import url
from django.contrib.auth import login, logout


from .views import (

                  create_tel,
                  phones,
	            )




urlpatterns = [

                url(r'^create_tel/$', create_tel, name="create_tel"),
                url(r'^phones/$', phones, name="phones"),





           ]