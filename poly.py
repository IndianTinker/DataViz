import json

with open("t.geojson") as x:
    data=json.load(x)

d=0.08

count = len(data['features'])

for i in range(0,count):
    x=data['features'][i]['geometry']['coordinates'][0]
    y=data['features'][i]['geometry']['coordinates'][1]

    x=x-d/2
    y=y-d/2

    del data['features'][i]['geometry']['coordinates'][0]
    del data['features'][i]['geometry']['coordinates'][0]

    data['features'][i]['geometry']['coordinates'].append([])

    data['features'][i]['geometry']['coordinates'][0].append([x,y])
    data['features'][i]['geometry']['coordinates'][0].append([x+d,y])
    data['features'][i]['geometry']['coordinates'][0].append([x+d,y+d])
    data['features'][i]['geometry']['coordinates'][0].append([x,y+d])
    data['features'][i]['geometry']['coordinates'][0].append([x,y])

    data['features'][i]['geometry']['type']=unicode('Polygon','utf-8')

    data['features'][i]['properties']['height']*=7000

o=open("poly.geojson",'w')
o.write(json.dumps(data))
o.close()
