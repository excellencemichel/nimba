from django.conf.urls import url
from .views import login



urlpatterns = [
      url(r'^login/$',login, name="login"),
      # url(r'^logout/', auth_views.logout, {"next_page": "accounts:login"}, name="logout"),
 
    ]