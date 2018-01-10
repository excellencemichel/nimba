from django.conf.urls import url
from .views import login, facebook_login



urlpatterns = [
      url(r'^login/$',login, name="login"),
      url(r'^facebook-login/$', facebook_login, name="facebook_login"),
      # url(r'^logout/', auth_views.logout, {"next_page": "accounts:login"}, name="logout"),
 
    ]