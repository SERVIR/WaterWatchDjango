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
def pondsList():

    xx =  ee.FeatureCollection(ponds.map(pondClassifier)).getInfo()
    names = []
    centers = []
    classes=[]
    return_obj = {}
    for feature in xx['features']:
        if feature['properties']['Nom']:
            name = feature['properties']['Nom']
            pclass= feature['properties']['pondCls']
            if len(feature['geometry']['coordinates'][0][0]) > 2:
                # print(len(feature['geometry']['coordinates'][0][0]))
                points = feature['geometry']['coordinates'][0][0]
            else:
                # print(len(feature['geometry']['coordinates'][0][0]))
                points = feature['geometry']['coordinates'][0]
            x = [p[0] for p in points if p[0] and p[1]]
            y = [p[1] for p in points if p[0] and p[1]]
            centroid = [sum(x) / len(points), sum(y) / len(points)]
            if name not in names:
                names.append(str(name))
                centers.append(centroid)
                classes.append(pclass)
    names, centers, classes = (list(t) for t in zip(*sorted(zip(names, centers, classes), reverse=False)))

    return names, centers, classes
return_obj={}
names, centers, classes = pondsList()
return_obj["centers"] = centers
return_obj["names"] = names
return_obj["classes"] = classes

with open(data['LIST_PATH'], "w") as outfile:
    json.dump(return_obj, outfile)