"""milienlaces URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic.base import RedirectView
from django.conf.urls import include

# TODO fix these endpoints ?!
urlpatterns = [
    path('admin/', admin.site.urls),
  #  path('login/', admin.site.urls), # TODO missing logout, reset pwd etc
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('enlaces.urls')),
#    path('user/<int:userid>/',  admin.site.urls),
#    path('link/<int:linkid>/<str:action>/', admin.site.urls),
    path('batch/opps/', admin.site.urls),
    path('batch/links/', admin.site.urls),
#    path('', RedirectView.as_view(url='user/')),
]
