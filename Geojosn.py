import json
from urllib.request import urlopen

with open(r"C:\Users\86753\Downloads\test-3.json") as f:
    j1 = json.load(f)


for features in j1:
    print(features)


with open(r"C:\Users\86753\Downloads\test-4.json", "w") as d:
    json.dump(j1,d)

with urlopen("https://developer.salesforce.com/files/la-zip-code-areas-2012.geojson") as response:
     source = response.read()

geoj=json.loads(source)

features= geoj["features"]

#for key1 in geoj.keys(): print(key1)

for key2 in features[0].keys(): print(key2)

for i in features:
     i['id'] = i["properties"]["external_id"]

for key2 in features[0].keys(): print(key2)

with open(r"C:\Users\86753\Downloads\test-4.json", "w") as d:
    json.dump(features,d)
