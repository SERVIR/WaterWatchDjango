import datetime
import locale

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .utilities import *
from . import candy


def set_locale(locale_):
    locale.setlocale(category=locale.LC_ALL, locale=locale_)


def date_customerprofile(dte):
    dt = datetime.datetime.strptime(dte, "%B %d, %Y")
    arr_dates=[]
    set_locale('fr_FR')
    date_ = dt.strftime("%B %d, %Y")
    arr_dates.append(date_)
    set_locale('en_US')
    date_ = dt.strftime("%B %d, %Y")
    arr_dates.append(date_)

    return arr_dates





@csrf_exempt
def getLastUpdatedDate(request):
    return_obj = {}
    if request.method == 'POST':
        info = request.POST
        lang = info.get('lang')
    with open(data['DATE_FILE']) as f:
        contents = f.read()
        dtes = date_customerprofile(contents)
        if 'English' in lang:
            return_obj["contents"] = dtes[1]
        else:
            return_obj["contents"] = dtes[0]
    return JsonResponse(return_obj)


@csrf_exempt
def getPondsUrl(request):
    print("from ponds url")
    return_obj = {}

    if request.method == 'POST':

        try:
            with open(data['JSON_PATH'], 'r') as openfile:
                json_object = json.load(openfile)
            return_obj["url"] = json_object["url"]
            # print(return_obj)
            return_obj["success"] = "success"

        except Exception as e:
            print(e)
            return_obj["error"] = candy.translated(request, "all_Error")
    return JsonResponse(return_obj)


@csrf_exempt
def getPondsList(request):
    return_obj = {}
    centers = []
    names = []

    if request.method == 'POST':

        try:
            names, centers, classes = pondsList()
            return_obj["centers"] = centers
            return_obj["names"] = names
            return_obj["classes"] = classes

            return_obj["success"] = "success"

        except Exception as e:
            return_obj["error"] = candy.translated(request, "all_Error")
    return JsonResponse(return_obj)


@csrf_exempt
def timeseries(request, lang):
    return_obj = {}

    if request.method == 'POST':
        info = request.POST
        lat = info.get('lat')
        lon = info.get('lon')

        try:
            ts_vals, coordinates, name = checkFeature(lon, lat)
            return_obj["values"] = ts_vals
            return_obj["msg"] = candy.translated(lang, "all_percent")
            return_obj["chart_msg"] = candy.translated(lang, "all_coverage")
            return_obj['chart_viewFullscreen'] = candy.translated(lang, "chart_viewFullscreen")
            return_obj['chart_printChart'] = candy.translated(lang, "chart_printChart")
            return_obj['chart_downloadPNG'] = candy.translated(lang, "chart_downloadPNG")
            return_obj['chart_downloadJPEG'] = candy.translated(lang, "chart_downloadJPEG")
            return_obj['chart_downloadPDF'] = candy.translated(lang, "chart_downloadPDF")
            return_obj['chart_downloadSVG'] = candy.translated(lang, "chart_downloadSVG")
            return_obj['chart_downloadCSV'] = candy.translated(lang, "chart_downloadCSV")
            return_obj['chart_downloadXLS'] = candy.translated(lang, "chart_downloadXLS")
            return_obj['chart_viewData'] = candy.translated(lang, "chart_viewData")
            return_obj['chart_all'] = candy.translated(lang, "chart_all")
            return_obj['chart_1month'] = candy.translated(lang, "chart_1month")
            return_obj['chart_3month'] = candy.translated(lang, "chart_3month")
            return_obj['chart_6month'] = candy.translated(lang, "chart_6month")
            return_obj['chart_1year'] = candy.translated(lang, "chart_1year")
            return_obj['chart_ytd'] = candy.translated(lang, "chart_ytd")
            return_obj['chart_weekdays'] = candy.translated(lang, "chart_weekdays")

            return_obj['chart_months'] = candy.translated(lang, "chart_months")

            return_obj['chart_shortMonths'] = candy.translated(lang, "chart_shortMonths")
            return_obj["coordinates"] = coordinates
            return_obj["name"] = name
            return_obj["success"] = "success"

        except Exception as e:
            return_obj["error"] = candy.translated(lang, "all_Error")
    return JsonResponse(return_obj)


@csrf_exempt
def forecast(request, lang):
    return_obj = {}
    if request.method == 'POST':
        info = request.POST
        lat = info.get('lat')
        lon = info.get('lon')
    try:

        ts_vals, coordinates, name = forecastFeature(lon, lat)
        return_obj["values"] = ts_vals
        return_obj["msg"] = candy.translated(lang, "all_percent")
        return_obj["fcast"] = candy.translated(lang, "all_forecast")
        return_obj["chart_msg"] = candy.translated(lang, "all_coverage")
        return_obj['chart_viewFullscreen'] = candy.translated(lang, "chart_viewFullscreen")
        return_obj['chart_printChart'] = candy.translated(lang, "chart_printChart")
        return_obj['chart_downloadPNG'] = candy.translated(lang, "chart_downloadPNG")
        return_obj['chart_downloadJPEG'] = candy.translated(lang, "chart_downloadJPEG")
        return_obj['chart_downloadPDF'] = candy.translated(lang, "chart_downloadPDF")
        return_obj['chart_downloadSVG'] = candy.translated(lang, "chart_downloadSVG")
        return_obj['chart_downloadCSV'] = candy.translated(lang, "chart_downloadCSV")
        return_obj['chart_downloadXLS'] = candy.translated(lang, "chart_downloadXLS")
        return_obj['chart_viewData'] = candy.translated(lang, "chart_viewData")
        return_obj['chart_all'] = candy.translated(lang, "chart_all")
        return_obj['chart_1month'] = candy.translated(lang, "chart_1month")
        return_obj['chart_3month'] = candy.translated(lang, "chart_3month")
        return_obj['chart_6month'] = candy.translated(lang, "chart_6month")
        return_obj['chart_1year'] = candy.translated(lang, "chart_1year")
        return_obj['chart_ytd'] = candy.translated(lang, "chart_ytd")
        return_obj['chart_weekdays'] = candy.translated(lang, "chart_weekdays")

        return_obj['chart_months'] = candy.translated(lang, "chart_months")

        return_obj['chart_shortMonths'] = candy.translated(lang, "chart_shortMonths")
        return_obj["coordinates"] = coordinates
        return_obj["name"] = name
        return_obj["success"] = "success"
    except Exception as e:
        return_obj["error"] = candy.translated(lang, "all_Error")
    return JsonResponse(return_obj)


@csrf_exempt
def mndwi(request):
    return_obj = {}

    if request.method == 'POST':

        info = request.POST
        x_val = info.get('xValue')
        y_val = info.get('yValue')
        clicked_date = datetime.datetime.fromtimestamp((int(x_val) / 1000)).strftime('%Y %B %d')
        lat = info.get('lat')
        lon = info.get('lon')

        try:
            true_img, mndwi_img, properties = getMNDWI(lon, lat, x_val, y_val)
            return_obj['water_mapurl'] = mndwi_img['tile_fetcher'].url_format
            return_obj['true_mapurl'] = true_img['tile_fetcher'].url_format
            return_obj["date"] = clicked_date
            return_obj["cloud_cover"] = properties["CLOUD_COVER"]
            return_obj["success"] = "success"

        except Exception as e:
            return_obj["error"] = candy.translated(request, "all_Error")

    return JsonResponse(return_obj)


@csrf_exempt
def details(request, lang):
    return_obj = {}

    if request.method == 'POST':
        info = request.POST
        lat = info.get('lat')
        lon = info.get('lon')

        try:
            ponds = filterPond(lon, lat)
            region = filterRegion(lon, lat)
            commune = filterCommune(lon, lat)
            arrondissement = filterArrondissement(lon, lat)
            namePond = ponds.getInfo()['features'][0]['properties']['Nom']
            if len(namePond) < 2:
                namePond = 'Unnamed Pond'

            coordinates = ponds.getInfo()['features'][0]['geometry']['coordinates']

            sup_Pond = ponds.getInfo()['features'][0]['properties']['Sup']
            nameRegion = region.getInfo()['features'][0]['properties']['nom']
            nameCommune = commune.getInfo()['features'][0]['properties']['nom']
            nameArrondissement = arrondissement.getInfo()['features'][0]['properties']['nom']

            return_obj["namePond"] = namePond
            return_obj["sup_Pond"] = sup_Pond
            return_obj["coordinates"] = coordinates
            return_obj["nameRegion"] = nameRegion
            return_obj["nameCommune"] = nameCommune
            return_obj["nameArrondissement"] = nameArrondissement
            return_obj["namePond_label"] = candy.translated(lang, "all_pname")
            return_obj["sup_Pond_label"] = candy.translated(lang, "all_area")
            return_obj["nameRegion_label"] = candy.translated(lang, "all_Rname")
            return_obj["nameCommune_label"] = candy.translated(lang, "all_cname")
            return_obj["nameArrondissement_label"] = candy.translated(lang, "all_Bname")
            return_obj["success"] = "success"
        except Exception as e:
            return_obj["error"] = candy.translated(lang, "all_Error")
        print("processing complete...")

    return JsonResponse(return_obj)


@csrf_exempt
def coucheVillages(request, lang):
    return_obj = {}
    if request.method == 'POST':
        try:
            village = checkVillage()
            return_obj["village"] = village
            return_obj['msg'] = candy.translated(lang, "all_Villages")
            return_obj['with'] = candy.translated(lang, "all_with")
            return_obj['inhabitants'] = candy.translated(lang, "all_inhabitants")
            return_obj["success"] = "success"
        except Exception as e:
            return_obj["error"] = candy.translated(lang, "all_Error")
    return JsonResponse(return_obj)
