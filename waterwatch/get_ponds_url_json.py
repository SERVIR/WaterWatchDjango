import json
from pathlib import Path
import ee
from ee import EEException
BASE_DIR = Path(__file__).resolve().parent.parent
f = open(str(BASE_DIR) + '/data.json', )
data = json.load(f)
try:
    credentials = ee.ServiceAccountCredentials(data['EE_SERVICE_ACCOUNT'],
                                               data['EE_SECRET_KEY'])
    ee.Initialize(credentials)

except EEException:
    ee.Initialize()

visParams = {'min': 0, 'max': 3, 'palette': 'red,#FF9300,green,gray'}
waterCollection = ee.ImageCollection("projects/servir-wa/services/ephemeral_water_ferlo/processed_ponds")

def addArea(feature):
    return feature.set('area', feature.area());
def pondClassifier(shape):
    waterList = waterCollection.filterBounds(shape.geometry()) \
        .sort('system:time_start', False)

    latest = ee.Image(waterList.reduce(ee.Reducer.firstNonNull()))

    avg = latest.select(".*_water_.*").reduceRegion(
        reducer=ee.Reducer.mean(),
        scale=30,
        maxPixels=1e5,
        geometry=shape.geometry(),
        # bestEffort=True
    )
    val = ee.Number(avg.values().reduce(ee.Reducer.mean()))
    temp = ee.Number(ee.Algorithms.If(val.gte(0), 0, 3));
    cls = temp.add(val.gt(0.25).uint8());
    cls = cls.add(val.gt(0.75).uint8());

    return ee.Feature(shape).set({'pondCls': cls})
ponds = ee.FeatureCollection('projects/servir-wa/services/ephemeral_water_ferlo/ferlo_ponds') \
    .map(addArea).filter(ee.Filter.gt("area", 10000))
ponds_cls = ee.FeatureCollection(ponds.map(pondClassifier))

# Pimage = ee.Image().paint(ponds,"pondCls").blend(
#     ee.Image().paint(ponds,"pondCls",1.5)
# )
Pimage = ponds_cls.reduceToImage(
    properties=['pondCls'],
    reducer=ee.Reducer.first()
)

def initLayers():
    pondsImgID = Pimage.getMapId(visParams)
    return pondsImgID['tile_fetcher'].url_format


ponds_url = {'url':initLayers()}
with open(data['JSON_PATH'], "w") as outfile:
    json.dump(ponds_url, outfile)