"""nimba URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static


from django.contrib import admin

from django.contrib.auth.views import (
            password_reset,
            password_reset_done,
            password_reset_confirm,
            password_reset_complete,
    )


from .views import home, hand

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', home, name="home"),
    url(r'^hand$', hand, name="hand"),


    url(r'^account/', include("accounts.urls", app_name="accounts", namespace="accounts")),


    url(r'^profile/', include("profile.urls", app_name="profile", namespace="profile")),
    url(r'^phone/', include("phone.urls", app_name="phone", namespace="phone")),
    url(r'^electromenager/', include("electromenager.urls", app_name="electromenager", namespace="electromenager")),



      url(r'^reset-password/$', password_reset, name="reset_password"),
      url(r'^reset-password/done/$', password_reset_done, name="password_reset_done"),
      url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, name="password_reset_confirm"),
      url(r'^reset-password/complete/$', password_reset_complete, name="password_reset_complete"), 



]




urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

