from django.conf.urls import url
from django.contrib.auth.views import (password_reset, password_reset_done,
                                      password_reset_confirm, password_reset_complete



                                      )

from .views import (
				home,
                register,
                activate,



		)



urlpatterns = [


                url(r'^register/$', register, name="register"),

                url(r'^activate/(?P<uidb64>[\w\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[\w]{1,20})/$', activate, name="active"),


]