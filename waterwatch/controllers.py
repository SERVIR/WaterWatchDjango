import json
from pathlib import Path

import ee
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from ee.ee_exception import EEException
from . import candy

from .utilities import initLayers, initMndwi, checkFeature

BASE_DIR = Path(__file__).resolve().parent.parent
f = open(str(BASE_DIR) + '/data.json', )
data = json.load(f)


def home(request):
    """
    Controller for the app home page.
    """
    try:
        credentials = ee.ServiceAccountCredentials(data['EE_SERVICE_ACCOUNT'],
                                                   data['EE_SECRET_KEY'])
        ee.Initialize(credentials)

    except EEException:
        ee.Initialize()

    ponds = initLayers()

    mndwi = initMndwi()
    context = {
        # 'ponds_mapurl': ponds['tile_fetcher'].url_format,
        'mndwiImg_mapid': mndwi,
    }
    return candy.render(request, 'waterwatch/home.html', context)
