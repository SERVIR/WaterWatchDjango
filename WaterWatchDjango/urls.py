"""WaterWatchDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from WaterWatchDjango import settings
from waterwatch import ajax_controllers, api, controllers

urlpatterns = [
    path('admin/', admin.site.urls),
path('get-ponds-list/', ajax_controllers.getPondsList,name="get-ponds-list"),
path('timeseries/', ajax_controllers.timeseries,name="timeseries"),
path('forecast/', ajax_controllers.forecast,name="forecast"),
path('mndwi/', ajax_controllers.mndwi,name="mndwi"),
path('api/getPonds/', api.api_get_ponds,name="getPonds"),
path('api/getTimeseries/',api.api_get_timeseries,name="getTimeseries"),

path('details/',ajax_controllers.details,name="details"),
path('coucheVillages/',ajax_controllers.coucheVillages,name="coucheVillages"),


path('get-ponds-url/', ajax_controllers.getPondsUrl,name="get-ponds-url"),

path('', controllers.home,name="home"),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

