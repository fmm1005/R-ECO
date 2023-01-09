import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred= credentials.Certificate("r-eco-90151-firebase-adminsdk-44bny-3bbe569a54.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
data={
  "type": "FeatureCollection",
  "generator": "overpass-ide",
  "copyright": "The data included in this document is from www.openstreetmap.org. The data is made available under ODbL.",
  "timestamp": "2023-01-09T11:14:09Z",
  "features": [
    {
      "type": "Feature",
      "properties": {
        "@id": "node/481186700",
        "amenity": "recycling",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7023699,
          42.3363621
        ]
      },
      "id": "node/481186700"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/520044711",
        "amenity": "recycling",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7041752,
          42.3355221
        ]
      },
      "id": "node/520044711"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/520058113",
        "amenity": "recycling",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7028801,
          42.3329462
        ]
      },
      "id": "node/520058113"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/522818469",
        "amenity": "recycling",
        "recycling:cans": "yes",
        "recycling:cooking_oil": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7022246,
          42.3384907
        ]
      },
      "id": "node/522818469"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/532453928",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.724348,
          42.3375791
        ]
      },
      "id": "node/532453928"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/532453954",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7269273,
          42.3376731
        ]
      },
      "id": "node/532453954"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/544529731",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7131987,
          42.3344615
        ]
      },
      "id": "node/544529731"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/544529737",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7148757,
          42.3344295
        ]
      },
      "id": "node/544529737"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/616834662",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.731507,
          42.342461
        ]
      },
      "id": "node/616834662"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/616846810",
        "amenity": "recycling",
        "recycling:cans": "yes",
        "recycling:cooking_oil": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7000511,
          42.332177
        ]
      },
      "id": "node/616846810"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/660717354",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.725747,
          42.3367561
        ]
      },
      "id": "node/660717354"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/664012087",
        "amenity": "recycling",
        "location": "underground",
        "recycling:glass_bottles": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7006829,
          42.341566
        ]
      },
      "id": "node/664012087"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/711721068",
        "amenity": "recycling",
        "recycling:beverage_cartons": "yes",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_bottles": "yes",
        "recycling:plastic_packaging": "no",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.682789,
          42.3466141
        ]
      },
      "id": "node/711721068"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/721207387",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7125231,
          42.3447176
        ]
      },
      "id": "node/721207387"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/745406251",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6583604,
          42.3632695
        ]
      },
      "id": "node/745406251"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/745406270",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6583772,
          42.3641127
        ]
      },
      "id": "node/745406270"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/745429139",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.659757,
          42.3639793
        ]
      },
      "id": "node/745429139"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/954995993",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7025854,
          42.3422307
        ]
      },
      "id": "node/954995993"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/966641111",
        "amenity": "recycling",
        "operator": "Urbaser",
        "recycling:books": "yes",
        "recycling:cartons": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:magazines": "yes",
        "recycling:newspaper": "yes",
        "recycling:organic": "yes",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6972943,
          42.335418
        ]
      },
      "id": "node/966641111"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/968568893",
        "amenity": "recycling",
        "recycling:cans": "yes",
        "recycling:cooking_oil": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6917084,
          42.3439122
        ]
      },
      "id": "node/968568893"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/1184311858",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6642738,
          42.3537018
        ]
      },
      "id": "node/1184311858"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/1184312835",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6624552,
          42.353896
        ]
      },
      "id": "node/1184312835"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/1487299642",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7258853,
          42.3381138
        ]
      },
      "id": "node/1487299642"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/1657525102",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.704373,
          42.3360311
        ]
      },
      "id": "node/1657525102"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/1665972454",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7337984,
          42.3492849
        ]
      },
      "id": "node/1665972454"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/1666034584",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7119698,
          42.3279683
        ]
      },
      "id": "node/1666034584"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/1666034587",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7111535,
          42.3290521
        ]
      },
      "id": "node/1666034587"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/1666034591",
        "amenity": "recycling",
        "location": "overground",
        "recycling:beverage_cartons": "yes",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_bottles": "yes",
        "recycling:plastic_packaging": "no",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7095218,
          42.3306965
        ]
      },
      "id": "node/1666034591"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/1666034596",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7071467,
          42.331724
        ]
      },
      "id": "node/1666034596"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/1666034607",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6907869,
          42.3421569
        ]
      },
      "id": "node/1666034607"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/1666034653",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7716256,
          42.3610362
        ]
      },
      "id": "node/1666034653"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/1666034655",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7744455,
          42.3613163
        ]
      },
      "id": "node/1666034655"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/1667462633",
        "amenity": "recycling",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.682446,
          42.3460223
        ]
      },
      "id": "node/1667462633"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/1667462654",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.669959,
          42.3529288
        ]
      },
      "id": "node/1667462654"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/1668712168",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6852672,
          42.3597018
        ]
      },
      "id": "node/1668712168"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/1707695826",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7008758,
          42.3272093
        ]
      },
      "id": "node/1707695826"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/1744604095",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7313079,
          42.3410253
        ]
      },
      "id": "node/1744604095"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/1744604119",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7298925,
          42.3421371
        ]
      },
      "id": "node/1744604119"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/1744676662",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.708227,
          42.3379019
        ]
      },
      "id": "node/1744676662"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/1744716655",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7069989,
          42.3364491
        ]
      },
      "id": "node/1744716655"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/1745560797",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7080202,
          42.3388274
        ]
      },
      "id": "node/1745560797"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/1745985562",
        "amenity": "recycling",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7052753,
          42.3390785
        ]
      },
      "id": "node/1745985562"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/1745985724",
        "amenity": "recycling",
        "location": "overground",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7075253,
          42.3393095
        ]
      },
      "id": "node/1745985724"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/1752809142",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7168855,
          42.3353834
        ]
      },
      "id": "node/1752809142"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/1752809576",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7134322,
          42.3359273
        ]
      },
      "id": "node/1752809576"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/1752859824",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.716846,
          42.3367452
        ]
      },
      "id": "node/1752859824"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/1754276667",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7275869,
          42.3421902
        ]
      },
      "id": "node/1754276667"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/1769278646",
        "amenity": "recycling",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7007651,
          42.3370474
        ]
      },
      "id": "node/1769278646"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/1770752293",
        "amenity": "recycling",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7008205,
          42.3390139
        ]
      },
      "id": "node/1770752293"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/1777465062",
        "amenity": "recycling",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7062317,
          42.3402704
        ]
      },
      "id": "node/1777465062"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/1829278502",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6832668,
          42.3477126
        ]
      },
      "id": "node/1829278502"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/1829281752",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.698706,
          42.3478017
        ]
      },
      "id": "node/1829281752"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/1829281754",
        "amenity": "recycling",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6978156,
          42.3486956
        ]
      },
      "id": "node/1829281754"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/1829281755",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6992766,
          42.3489279
        ]
      },
      "id": "node/1829281755"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/1829281756",
        "amenity": "recycling",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6948646,
          42.3491851
        ]
      },
      "id": "node/1829281756"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/1829281757",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6961569,
          42.3499564
        ]
      },
      "id": "node/1829281757"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/1829281858",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6927953,
          42.3495049
        ]
      },
      "id": "node/1829281858"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/1985808434",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6655732,
          42.3533426
        ]
      },
      "id": "node/1985808434"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/2288533093",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7373912,
          42.3492195
        ]
      },
      "id": "node/2288533093"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/2912374382",
        "amenity": "recycling",
        "recycling:cans": "yes",
        "recycling:green_waste": "yes",
        "recycling:paper": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7105526,
          42.3355165
        ]
      },
      "id": "node/2912374382"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/3193764262",
        "amenity": "recycling",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7074256,
          42.3419345
        ]
      },
      "id": "node/3193764262"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/3193764271",
        "amenity": "recycling",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6889693,
          42.3429035
        ]
      },
      "id": "node/3193764271"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/3534232259",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6918335,
          42.3472116
        ]
      },
      "id": "node/3534232259"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/3881765680",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6627512,
          42.3517517
        ]
      },
      "id": "node/3881765680"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/3927190814",
        "amenity": "recycling",
        "recycling:cartons": "yes",
        "recycling:paper": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6971254,
          42.2942572
        ]
      },
      "id": "node/3927190814"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4222733023",
        "amenity": "recycling",
        "operator": "Cáritas Diocesana de Burgos",
        "recycling:clothes": "yes",
        "recycling:shoes": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6949137,
          42.3382966
        ]
      },
      "id": "node/4222733023"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4471062822",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6949728,
          42.3443341
        ]
      },
      "id": "node/4471062822"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4669348224",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7129993,
          42.3496753
        ]
      },
      "id": "node/4669348224"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4669348226",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7159793,
          42.349368
        ]
      },
      "id": "node/4669348226"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4672317820",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7141852,
          42.3480874
        ]
      },
      "id": "node/4672317820"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4672317821",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7180719,
          42.3481446
        ]
      },
      "id": "node/4672317821"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4684296445",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.71527,
          42.3467436
        ]
      },
      "id": "node/4684296445"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4684296446",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7142763,
          42.3445322
        ]
      },
      "id": "node/4684296446"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4684296447",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7142548,
          42.343531
        ]
      },
      "id": "node/4684296447"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4684296448",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6870438,
          42.3596886
        ]
      },
      "id": "node/4684296448"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4684296449",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6799265,
          42.3571967
        ]
      },
      "id": "node/4684296449"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4684296450",
        "amenity": "recycling",
        "location": "overground",
        "recycling:beverage_cartons": "yes",
        "recycling:cans": "yes",
        "recycling:cardboard": "yes",
        "recycling:cartons": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic_bottles": "yes",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6773221,
          42.3549907
        ]
      },
      "id": "node/4684296450"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4684296451",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6744629,
          42.3496219
        ]
      },
      "id": "node/4684296451"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4684296452",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6720113,
          42.3499014
        ]
      },
      "id": "node/4684296452"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4684296453",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6726658,
          42.3503167
        ]
      },
      "id": "node/4684296453"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4684296469",
        "amenity": "recycling",
        "mapillary": "314528536867878",
        "recycling_type": "container",
        "survey:date": "2019-01-09"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7563829,
          42.3547454
        ]
      },
      "id": "node/4684296469"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4684296471",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.77395,
          42.3601826
        ]
      },
      "id": "node/4684296471"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4684296614",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6634457,
          42.3286583
        ]
      },
      "id": "node/4684296614"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4684296615",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.665511,
          42.3279186
        ]
      },
      "id": "node/4684296615"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4684296616",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6647922,
          42.3264859
        ]
      },
      "id": "node/4684296616"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4684296617",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6627953,
          42.3275677
        ]
      },
      "id": "node/4684296617"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4684296618",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6269073,
          42.3425685
        ]
      },
      "id": "node/4684296618"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4684296619",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6270116,
          42.3443961
        ]
      },
      "id": "node/4684296619"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4684296621",
        "amenity": "recycling",
        "recycling:glass_bottles": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6158846,
          42.3645085
        ]
      },
      "id": "node/4684296621"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4684296622",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6140689,
          42.3651333
        ]
      },
      "id": "node/4684296622"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4684296623",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6168437,
          42.3657868
        ]
      },
      "id": "node/4684296623"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4684296624",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6047402,
          42.3863473
        ]
      },
      "id": "node/4684296624"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4685814756",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7188816,
          42.3445056
        ]
      },
      "id": "node/4685814756"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4685814759",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7151855,
          42.3416585
        ]
      },
      "id": "node/4685814759"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4685814760",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7148532,
          42.3420502
        ]
      },
      "id": "node/4685814760"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4685814761",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7138913,
          42.3411878
        ]
      },
      "id": "node/4685814761"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4685814762",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7132627,
          42.3418749
        ]
      },
      "id": "node/4685814762"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4685814904",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6916209,
          42.3741057
        ]
      },
      "id": "node/4685814904"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4685814905",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6926672,
          42.3763593
        ]
      },
      "id": "node/4685814905"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4685814907",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6970826,
          42.3751633
        ]
      },
      "id": "node/4685814907"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4685814908",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6950891,
          42.3744933
        ]
      },
      "id": "node/4685814908"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4689493406",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7144634,
          42.3514141
        ]
      },
      "id": "node/4689493406"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4689493408",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7159949,
          42.342773
        ]
      },
      "id": "node/4689493408"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4689493409",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7211843,
          42.3450744
        ]
      },
      "id": "node/4689493409"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4689493410",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7244928,
          42.3442661
        ]
      },
      "id": "node/4689493410"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4689493411",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7262188,
          42.3448561
        ]
      },
      "id": "node/4689493411"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4689493412",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7220869,
          42.345144
        ]
      },
      "id": "node/4689493412"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4689493413",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7208189,
          42.3464933
        ]
      },
      "id": "node/4689493413"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4689493414",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7201832,
          42.3451601
        ]
      },
      "id": "node/4689493414"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4689493415",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7174876,
          42.3462396
        ]
      },
      "id": "node/4689493415"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4689493416",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.718661,
          42.3489915
        ]
      },
      "id": "node/4689493416"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4689493417",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7098902,
          42.344836
        ]
      },
      "id": "node/4689493417"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4689493418",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7122143,
          42.3443354
        ]
      },
      "id": "node/4689493418"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4689493419",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7131169,
          42.3433224
        ]
      },
      "id": "node/4689493419"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4689493420",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7180723,
          42.3422865
        ]
      },
      "id": "node/4689493420"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4689493421",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7183284,
          42.3417706
        ]
      },
      "id": "node/4689493421"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4689493422",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7138874,
          42.3401302
        ]
      },
      "id": "node/4689493422"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4689493423",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7112829,
          42.3401719
        ]
      },
      "id": "node/4689493423"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4689493424",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7342607,
          42.3478173
        ]
      },
      "id": "node/4689493424"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4689493425",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7300993,
          42.3484751
        ]
      },
      "id": "node/4689493425"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4689493426",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7388687,
          42.3504661
        ]
      },
      "id": "node/4689493426"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4689493427",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7402876,
          42.34927
        ]
      },
      "id": "node/4689493427"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4689493428",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.742821,
          42.3507979
        ]
      },
      "id": "node/4689493428"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4689493429",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7447864,
          42.3513923
        ]
      },
      "id": "node/4689493429"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4689493430",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7449768,
          42.3479753
        ]
      },
      "id": "node/4689493430"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4689493431",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7399047,
          42.3417411
        ]
      },
      "id": "node/4689493431"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4689493432",
        "amenity": "recycling",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7426258,
          42.3436101
        ]
      },
      "id": "node/4689493432"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4689493433",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7397948,
          42.3437479
        ]
      },
      "id": "node/4689493433"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4689493434",
        "amenity": "recycling",
        "recycling:cooking_oil": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.737995,
          42.3434931
        ]
      },
      "id": "node/4689493434"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4689493435",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7314296,
          42.3438034
        ]
      },
      "id": "node/4689493435"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4689493436",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7362375,
          42.3422499
        ]
      },
      "id": "node/4689493436"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4689493438",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7339013,
          42.3411981
        ]
      },
      "id": "node/4689493438"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4689493439",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7308798,
          42.3399826
        ]
      },
      "id": "node/4689493439"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4689493440",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7324992,
          42.3397171
        ]
      },
      "id": "node/4689493440"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4697370735",
        "amenity": "recycling",
        "mapillary": "2808334502797540",
        "recycling:paper": "yes",
        "recycling_type": "container",
        "survey:date": "2019-01-11"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6565189,
          42.3634841
        ]
      },
      "id": "node/4697370735"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4697370736",
        "amenity": "recycling",
        "mapillary": "1377813839251939",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "yes",
        "recycling_type": "container",
        "survey:date": "2019-01-11"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6576294,
          42.3624516
        ]
      },
      "id": "node/4697370736"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4697722225",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6737128,
          42.3523053
        ]
      },
      "id": "node/4697722225"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4697722226",
        "amenity": "recycling",
        "location": "overground",
        "recycling:beverage_cartons": "yes",
        "recycling:cans": "yes",
        "recycling:cardboard": "yes",
        "recycling:cartons": "yes",
        "recycling:paper": "yes",
        "recycling:plastic_bottles": "yes",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6870473,
          42.3518311
        ]
      },
      "id": "node/4697722226"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4697722227",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.683252,
          42.3476693
        ]
      },
      "id": "node/4697722227"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4697722228",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6761059,
          42.3493248
        ]
      },
      "id": "node/4697722228"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4697722229",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6745422,
          42.3503932
        ]
      },
      "id": "node/4697722229"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4697722230",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.673755,
          42.3508372
        ]
      },
      "id": "node/4697722230"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4697722232",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6805135,
          42.3470994
        ]
      },
      "id": "node/4697722232"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4697722233",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6842934,
          42.345006
        ]
      },
      "id": "node/4697722233"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4697961217",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6884329,
          42.3482679
        ]
      },
      "id": "node/4697961217"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4699613069",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7095418,
          42.3403777
        ]
      },
      "id": "node/4699613069"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4699613070",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7083885,
          42.3407415
        ]
      },
      "id": "node/4699613070"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4699613086",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6989948,
          42.3445021
        ]
      },
      "id": "node/4699613086"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4699613087",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.703415,
          42.3452361
        ]
      },
      "id": "node/4699613087"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4701881846",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7293793,
          42.3401175
        ]
      },
      "id": "node/4701881846"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4701881847",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.726685,
          42.3384127
        ]
      },
      "id": "node/4701881847"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4701881848",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7213072,
          42.337235
        ]
      },
      "id": "node/4701881848"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4701881849",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7190246,
          42.3367572
        ]
      },
      "id": "node/4701881849"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4701881850",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.714198,
          42.3373505
        ]
      },
      "id": "node/4701881850"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4701881851",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7158583,
          42.339352
        ]
      },
      "id": "node/4701881851"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4701881852",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7232061,
          42.3417869
        ]
      },
      "id": "node/4701881852"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4701881853",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7254283,
          42.3418707
        ]
      },
      "id": "node/4701881853"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4701881854",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.720375,
          42.3396111
        ]
      },
      "id": "node/4701881854"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4701881855",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7216544,
          42.3381935
        ]
      },
      "id": "node/4701881855"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4701881856",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7171242,
          42.3384681
        ]
      },
      "id": "node/4701881856"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4701881857",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7199834,
          42.3342667
        ]
      },
      "id": "node/4701881857"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4701881858",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7140262,
          42.3358044
        ]
      },
      "id": "node/4701881858"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4701881859",
        "amenity": "recycling",
        "location": "overground",
        "recycling:glass_bottles": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7100538,
          42.3346077
        ]
      },
      "id": "node/4701881859"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4701881860",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7091164,
          42.3363759
        ]
      },
      "id": "node/4701881860"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4701881861",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7058898,
          42.3353525
        ]
      },
      "id": "node/4701881861"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4701881862",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7044212,
          42.3342437
        ]
      },
      "id": "node/4701881862"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4701881864",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7084325,
          42.3320165
        ]
      },
      "id": "node/4701881864"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4701881865",
        "amenity": "recycling",
        "location": "overground",
        "recycling:glass_bottles": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7121178,
          42.3277667
        ]
      },
      "id": "node/4701881865"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4701881866",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7078967,
          42.3304334
        ]
      },
      "id": "node/4701881866"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4701881867",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7057872,
          42.3325432
        ]
      },
      "id": "node/4701881867"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4701881868",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7058985,
          42.3315548
        ]
      },
      "id": "node/4701881868"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4701881869",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7047612,
          42.332916
        ]
      },
      "id": "node/4701881869"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4701881870",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7039901,
          42.3314968
        ]
      },
      "id": "node/4701881870"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4701881871",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.702826,
          42.3313342
        ]
      },
      "id": "node/4701881871"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4701881872",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7024639,
          42.3302743
        ]
      },
      "id": "node/4701881872"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4701881873",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7021018,
          42.3312915
        ]
      },
      "id": "node/4701881873"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4701881874",
        "amenity": "recycling",
        "location": "overground",
        "recycling:glass_bottles": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7030889,
          42.3326527
        ]
      },
      "id": "node/4701881874"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4701881875",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7010195,
          42.3297583
        ]
      },
      "id": "node/4701881875"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4701881876",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7012234,
          42.331526
        ]
      },
      "id": "node/4701881876"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4701881877",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.70143,
          42.3322377
        ]
      },
      "id": "node/4701881877"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4701881878",
        "amenity": "recycling",
        "location": "overground",
        "recycling:beverage_cartons": "yes",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_bottles": "yes",
        "recycling:plastic_packaging": "no",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7023632,
          42.3341116
        ]
      },
      "id": "node/4701881878"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4701881879",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6992478,
          42.3315711
        ]
      },
      "id": "node/4701881879"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4701881880",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6996582,
          42.3289259
        ]
      },
      "id": "node/4701881880"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4701881881",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6991338,
          42.3272568
        ]
      },
      "id": "node/4701881881"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4701881882",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6964422,
          42.3246763
        ]
      },
      "id": "node/4701881882"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4701881883",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6974829,
          42.3284614
        ]
      },
      "id": "node/4701881883"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4701881884",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6985826,
          42.3308563
        ]
      },
      "id": "node/4701881884"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4701881885",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6977853,
          42.3328894
        ]
      },
      "id": "node/4701881885"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4701881886",
        "amenity": "recycling",
        "check_date:recycling": "2022-01-20",
        "location": "overground",
        "operator": "Urbaser",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6986239,
          42.3342764
        ]
      },
      "id": "node/4701881886"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4701881887",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7000008,
          42.3350368
        ]
      },
      "id": "node/4701881887"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4701881888",
        "amenity": "recycling",
        "location": "overground",
        "recycling:beverage_cartons": "yes",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_bottles": "yes",
        "recycling:plastic_packaging": "no",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7043353,
          42.3375583
        ]
      },
      "id": "node/4701881888"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4701883090",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6990554,
          42.337879
        ]
      },
      "id": "node/4701883090"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4701883091",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6989046,
          42.3392951
        ]
      },
      "id": "node/4701883091"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4701883092",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6994624,
          42.3386497
        ]
      },
      "id": "node/4701883092"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4701883093",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7008893,
          42.3383253
        ]
      },
      "id": "node/4701883093"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4701883096",
        "amenity": "recycling",
        "recycling:glass_bottles": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7035461,
          42.3378113
        ]
      },
      "id": "node/4701883096"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4704073548",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6945146,
          42.3326584
        ]
      },
      "id": "node/4704073548"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4704073549",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6896422,
          42.3348627
        ]
      },
      "id": "node/4704073549"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4704073550",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6965368,
          42.3334544
        ]
      },
      "id": "node/4704073550"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4704073551",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.693349,
          42.3346114
        ]
      },
      "id": "node/4704073551"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4704073552",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6948954,
          42.3350024
        ]
      },
      "id": "node/4704073552"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4704073553",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6928041,
          42.3356843
        ]
      },
      "id": "node/4704073553"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4704073555",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6918819,
          42.3366035
        ]
      },
      "id": "node/4704073555"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4704073556",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6914004,
          42.3363378
        ]
      },
      "id": "node/4704073556"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4704073557",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6886203,
          42.3373158
        ]
      },
      "id": "node/4704073557"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4704073558",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6877928,
          42.3379899
        ]
      },
      "id": "node/4704073558"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4704073559",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6987913,
          42.3362265
        ]
      },
      "id": "node/4704073559"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4704073560",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6980087,
          42.3371733
        ]
      },
      "id": "node/4704073560"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4704073561",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6966482,
          42.3373692
        ]
      },
      "id": "node/4704073561"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4704073562",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.694672,
          42.3375163
        ]
      },
      "id": "node/4704073562"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4704073563",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6914453,
          42.3381686
        ]
      },
      "id": "node/4704073563"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4704073564",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6858653,
          42.3401377
        ]
      },
      "id": "node/4704073564"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4704073565",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6883159,
          42.3396161
        ]
      },
      "id": "node/4704073565"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4704073566",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6902216,
          42.3400473
        ]
      },
      "id": "node/4704073566"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4704073567",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6812898,
          42.3411065
        ]
      },
      "id": "node/4704073567"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4704073568",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6923673,
          42.3400781
        ]
      },
      "id": "node/4704073568"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4704073569",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6926825,
          42.3386199
        ]
      },
      "id": "node/4704073569"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4704073570",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6949691,
          42.3385098
        ]
      },
      "id": "node/4704073570"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4704073571",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6959038,
          42.338717
        ]
      },
      "id": "node/4704073571"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4704073572",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6976795,
          42.3384692
        ]
      },
      "id": "node/4704073572"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4704073573",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7108084,
          42.3607462
        ]
      },
      "id": "node/4704073573"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4704073574",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6946435,
          42.3546459
        ]
      },
      "id": "node/4704073574"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4704073575",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6930247,
          42.3536375
        ]
      },
      "id": "node/4704073575"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4704073576",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6931991,
          42.3547991
        ]
      },
      "id": "node/4704073576"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4704235106",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:cooking_oil": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6997285,
          42.3453352
        ]
      },
      "id": "node/4704235106"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4704235107",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7005399,
          42.3473233
        ]
      },
      "id": "node/4704235107"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4704235108",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.698769,
          42.3468771
        ]
      },
      "id": "node/4704235108"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4704235109",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6982862,
          42.3477671
        ]
      },
      "id": "node/4704235109"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4704235110",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6970054,
          42.3505166
        ]
      },
      "id": "node/4704235110"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4704235111",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6962705,
          42.3511588
        ]
      },
      "id": "node/4704235111"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4704235112",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6954712,
          42.350918
        ]
      },
      "id": "node/4704235112"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4704235113",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6966809,
          42.3482905
        ]
      },
      "id": "node/4704235113"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4704235114",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6971972,
          42.3471586
        ]
      },
      "id": "node/4704235114"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4704235115",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6982178,
          42.3449521
        ]
      },
      "id": "node/4704235115"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4704235116",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6980193,
          42.3438474
        ]
      },
      "id": "node/4704235116"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4704235117",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:cooking_oil": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6971536,
          42.3459461
        ]
      },
      "id": "node/4704235117"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4704235118",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6962524,
          42.3470374
        ]
      },
      "id": "node/4704235118"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4704235119",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6964495,
          42.3451288
        ]
      },
      "id": "node/4704235119"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4704235120",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6933931,
          42.348121
        ]
      },
      "id": "node/4704235120"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4704235121",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.692217,
          42.3488039
        ]
      },
      "id": "node/4704235121"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4704235122",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6903649,
          42.3498922
        ]
      },
      "id": "node/4704235122"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4704235123",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6953726,
          42.3482132
        ]
      },
      "id": "node/4704235123"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4704235124",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6943856,
          42.3478167
        ]
      },
      "id": "node/4704235124"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4704235125",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6958675,
          42.3486376
        ]
      },
      "id": "node/4704235125"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4704235126",
        "amenity": "recycling",
        "location": "overground",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6940074,
          42.3504821
        ]
      },
      "id": "node/4704235126"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4704235127",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6916725,
          42.3506387
        ]
      },
      "id": "node/4704235127"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4704235128",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.690487,
          42.3507527
        ]
      },
      "id": "node/4704235128"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4704235129",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6907713,
          42.3514336
        ]
      },
      "id": "node/4704235129"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4704235130",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6919206,
          42.3526963
        ]
      },
      "id": "node/4704235130"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4704235131",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6909505,
          42.3530423
        ]
      },
      "id": "node/4704235131"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4704235132",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6900076,
          42.3512585
        ]
      },
      "id": "node/4704235132"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705187930",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6964955,
          42.3436362
        ]
      },
      "id": "node/4705187930"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705187931",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6957978,
          42.3448206
        ]
      },
      "id": "node/4705187931"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705187932",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6946109,
          42.3461379
        ]
      },
      "id": "node/4705187932"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705187933",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6924128,
          42.3479082
        ]
      },
      "id": "node/4705187933"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705187934",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6901128,
          42.3492725
        ]
      },
      "id": "node/4705187934"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705187935",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6943541,
          42.3450789
        ]
      },
      "id": "node/4705187935"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705187936",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6939873,
          42.3465669
        ]
      },
      "id": "node/4705187936"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705187937",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6909725,
          42.3480903
        ]
      },
      "id": "node/4705187937"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705187938",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6902215,
          42.3468276
        ]
      },
      "id": "node/4705187938"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705187939",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6877801,
          42.3470538
        ]
      },
      "id": "node/4705187939"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705187940",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6901612,
          42.3457242
        ]
      },
      "id": "node/4705187940"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705187941",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6914258,
          42.3451138
        ]
      },
      "id": "node/4705187941"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705187942",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6872333,
          42.3458639
        ]
      },
      "id": "node/4705187942"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705187943",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6877874,
          42.3450672
        ]
      },
      "id": "node/4705187943"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705187944",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6886189,
          42.3439114
        ]
      },
      "id": "node/4705187944"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705187945",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6903583,
          42.3449235
        ]
      },
      "id": "node/4705187945"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705187946",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6896891,
          42.3445171
        ]
      },
      "id": "node/4705187946"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705187947",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.693813,
          42.3442643
        ]
      },
      "id": "node/4705187947"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705187948",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6928916,
          42.3437033
        ]
      },
      "id": "node/4705187948"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705187949",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6938304,
          42.3435923
        ]
      },
      "id": "node/4705187949"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705187950",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6946163,
          42.3434694
        ]
      },
      "id": "node/4705187950"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705187951",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6945854,
          42.342717
        ]
      },
      "id": "node/4705187951"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705187952",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.697682,
          42.341013
        ]
      },
      "id": "node/4705187952"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705187953",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6950642,
          42.3420925
        ]
      },
      "id": "node/4705187953"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705187954",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6879014,
          42.3429271
        ]
      },
      "id": "node/4705187954"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705187955",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.68801,
          42.3435843
        ]
      },
      "id": "node/4705187955"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705187956",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6862638,
          42.3433831
        ]
      },
      "id": "node/4705187956"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705187957",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6934249,
          42.341699
        ]
      },
      "id": "node/4705187957"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705187958",
        "amenity": "recycling",
        "location": "overground",
        "recycling:glass_bottles": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6960601,
          42.3411714
        ]
      },
      "id": "node/4705187958"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705187959",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6868488,
          42.3449291
        ]
      },
      "id": "node/4705187959"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705472969",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6922291,
          42.3560077
        ]
      },
      "id": "node/4705472969"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705472970",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6900525,
          42.3566811
        ]
      },
      "id": "node/4705472970"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705472971",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6893887,
          42.3571489
        ]
      },
      "id": "node/4705472971"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705472972",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.688036,
          42.3583162
        ]
      },
      "id": "node/4705472972"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705472973",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6860257,
          42.3590178
        ]
      },
      "id": "node/4705472973"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705472974",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6889354,
          42.3567832
        ]
      },
      "id": "node/4705472974"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705472975",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6858022,
          42.3562256
        ]
      },
      "id": "node/4705472975"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705472976",
        "amenity": "recycling",
        "location": "overground",
        "recycling:beverage_cartons": "yes",
        "recycling:cans": "yes",
        "recycling:cardboard": "yes",
        "recycling:cartons": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic_bottles": "yes",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6888509,
          42.3532957
        ]
      },
      "id": "node/4705472976"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705472977",
        "amenity": "recycling",
        "location": "overground",
        "recycling:beverage_cartons": "yes",
        "recycling:cans": "yes",
        "recycling:cardboard": "yes",
        "recycling:cartons": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic_bottles": "yes",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6877626,
          42.3529195
        ]
      },
      "id": "node/4705472977"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705472978",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6903489,
          42.3524964
        ]
      },
      "id": "node/4705472978"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705472979",
        "amenity": "recycling",
        "location": "overground",
        "recycling:beverage_cartons": "yes",
        "recycling:cans": "yes",
        "recycling:cardboard": "yes",
        "recycling:cartons": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic_bottles": "yes",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6883909,
          42.3510314
        ]
      },
      "id": "node/4705472979"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705472980",
        "amenity": "recycling",
        "location": "overground",
        "recycling:beverage_cartons": "yes",
        "recycling:cans": "yes",
        "recycling:cardboard": "yes",
        "recycling:cartons": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic_bottles": "yes",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6854192,
          42.3528319
        ]
      },
      "id": "node/4705472980"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705472981",
        "amenity": "recycling",
        "location": "overground",
        "recycling:beverage_cartons": "yes",
        "recycling:cans": "yes",
        "recycling:cardboard": "yes",
        "recycling:cartons": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic_bottles": "yes",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6870839,
          42.3546086
        ]
      },
      "id": "node/4705472981"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705472983",
        "amenity": "recycling",
        "location": "overground",
        "recycling:beverage_cartons": "yes",
        "recycling:cans": "yes",
        "recycling:cardboard": "yes",
        "recycling:cartons": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic_bottles": "yes",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6808791,
          42.3557743
        ]
      },
      "id": "node/4705472983"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705472984",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6817095,
          42.3567157
        ]
      },
      "id": "node/4705472984"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705472985",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6816431,
          42.3600114
        ]
      },
      "id": "node/4705472985"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705472986",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6810175,
          42.3603438
        ]
      },
      "id": "node/4705472986"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705472987",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6798226,
          42.3609661
        ]
      },
      "id": "node/4705472987"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705472988",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6787685,
          42.3625625
        ]
      },
      "id": "node/4705472988"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705473189",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.68006,
          42.3622741
        ]
      },
      "id": "node/4705473189"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705473190",
        "amenity": "recycling",
        "location": "overground",
        "recycling:beverage_cartons": "yes",
        "recycling:cans": "yes",
        "recycling:cardboard": "yes",
        "recycling:cartons": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:organic": "yes",
        "recycling:paper": "yes",
        "recycling:plastic_bottles": "yes",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.67751,
          42.3597578
        ]
      },
      "id": "node/4705473190"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705473191",
        "amenity": "recycling",
        "location": "overground",
        "recycling:beverage_cartons": "yes",
        "recycling:cans": "yes",
        "recycling:cardboard": "yes",
        "recycling:cartons": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:organic": "yes",
        "recycling:paper": "yes",
        "recycling:plastic_bottles": "yes",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6790139,
          42.3599969
        ]
      },
      "id": "node/4705473191"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705473192",
        "amenity": "recycling",
        "location": "overground",
        "recycling:beverage_cartons": "yes",
        "recycling:cans": "yes",
        "recycling:cardboard": "yes",
        "recycling:cartons": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:organic": "yes",
        "recycling:paper": "yes",
        "recycling:plastic_bottles": "yes",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6798333,
          42.3594372
        ]
      },
      "id": "node/4705473192"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705473193",
        "amenity": "recycling",
        "location": "overground",
        "recycling:beverage_cartons": "yes",
        "recycling:cans": "yes",
        "recycling:cardboard": "yes",
        "recycling:cartons": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:organic": "yes",
        "recycling:paper": "yes",
        "recycling:plastic_bottles": "yes",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6810541,
          42.3589484
        ]
      },
      "id": "node/4705473193"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705473194",
        "amenity": "recycling",
        "location": "overground",
        "recycling:beverage_cartons": "yes",
        "recycling:cans": "yes",
        "recycling:cardboard": "yes",
        "recycling:cartons": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:organic": "yes",
        "recycling:paper": "yes",
        "recycling:plastic_bottles": "yes",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6777653,
          42.3604647
        ]
      },
      "id": "node/4705473194"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705473195",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6787363,
          42.3616677
        ]
      },
      "id": "node/4705473195"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705473196",
        "amenity": "recycling",
        "location": "overground",
        "recycling:beverage_cartons": "yes",
        "recycling:cans": "yes",
        "recycling:cardboard": "yes",
        "recycling:cartons": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:organic": "yes",
        "recycling:paper": "yes",
        "recycling:plastic_bottles": "yes",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6765188,
          42.3599015
        ]
      },
      "id": "node/4705473196"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705473197",
        "amenity": "recycling",
        "location": "overground",
        "recycling:beverage_cartons": "yes",
        "recycling:cans": "yes",
        "recycling:cardboard": "yes",
        "recycling:cartons": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:organic": "yes",
        "recycling:paper": "yes",
        "recycling:plastic_bottles": "yes",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6757399,
          42.3597898
        ]
      },
      "id": "node/4705473197"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705473198",
        "amenity": "recycling",
        "location": "overground",
        "recycling:beverage_cartons": "yes",
        "recycling:cans": "yes",
        "recycling:cardboard": "yes",
        "recycling:cartons": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:organic": "yes",
        "recycling:paper": "yes",
        "recycling:plastic_bottles": "yes",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6766678,
          42.3610531
        ]
      },
      "id": "node/4705473198"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705473199",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6770947,
          42.3623377
        ]
      },
      "id": "node/4705473199"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705473200",
        "amenity": "recycling",
        "location": "overground",
        "recycling:beverage_cartons": "yes",
        "recycling:cans": "yes",
        "recycling:cardboard": "yes",
        "recycling:cartons": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:organic": "yes",
        "recycling:paper": "yes",
        "recycling:plastic_bottles": "yes",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6754155,
          42.362376
        ]
      },
      "id": "node/4705473200"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705473201",
        "amenity": "recycling",
        "location": "overground",
        "recycling:beverage_cartons": "yes",
        "recycling:cans": "yes",
        "recycling:cardboard": "yes",
        "recycling:cartons": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:organic": "yes",
        "recycling:paper": "yes",
        "recycling:plastic_bottles": "yes",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6743563,
          42.3597651
        ]
      },
      "id": "node/4705473201"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705473203",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6890531,
          42.3501055
        ]
      },
      "id": "node/4705473203"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705473204",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6872819,
          42.3480425
        ]
      },
      "id": "node/4705473204"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705473205",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6844388,
          42.350331
        ]
      },
      "id": "node/4705473205"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705473206",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6833792,
          42.3527847
        ]
      },
      "id": "node/4705473206"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705473207",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6844427,
          42.3519274
        ]
      },
      "id": "node/4705473207"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705473208",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6854043,
          42.3511345
        ]
      },
      "id": "node/4705473208"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705473209",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6859313,
          42.3493346
        ]
      },
      "id": "node/4705473209"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705473210",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6860829,
          42.3468507
        ]
      },
      "id": "node/4705473210"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705473211",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6843111,
          42.3478521
        ]
      },
      "id": "node/4705473211"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705473212",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6823343,
          42.3518087
        ]
      },
      "id": "node/4705473212"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705473213",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6821304,
          42.3505995
        ]
      },
      "id": "node/4705473213"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705473214",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6821009,
          42.3483586
        ]
      },
      "id": "node/4705473214"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705473215",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6845533,
          42.3457791
        ]
      },
      "id": "node/4705473215"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705473216",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6803838,
          42.3485821
        ]
      },
      "id": "node/4705473216"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705473217",
        "amenity": "recycling",
        "location": "overground",
        "recycling:beverage_cartons": "yes",
        "recycling:cans": "yes",
        "recycling:cardboard": "yes",
        "recycling:cartons": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic_bottles": "yes",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.679688,
          42.355136
        ]
      },
      "id": "node/4705473217"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705473218",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6771563,
          42.3528979
        ]
      },
      "id": "node/4705473218"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705473219",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6786313,
          42.3527418
        ]
      },
      "id": "node/4705473219"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705473220",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6808912,
          42.3524953
        ]
      },
      "id": "node/4705473220"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705473221",
        "amenity": "recycling",
        "location": "overground",
        "recycling:beverage_cartons": "yes",
        "recycling:cans": "yes",
        "recycling:cardboard": "yes",
        "recycling:cartons": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:organic": "yes",
        "recycling:paper": "yes",
        "recycling:plastic_bottles": "yes",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6808255,
          42.3535637
        ]
      },
      "id": "node/4705473221"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705473222",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6816527,
          42.344738
        ]
      },
      "id": "node/4705473222"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705473223",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6827578,
          42.3444288
        ]
      },
      "id": "node/4705473223"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705473224",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.680022,
          42.3461837
        ]
      },
      "id": "node/4705473224"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705473226",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6783776,
          42.347048
        ]
      },
      "id": "node/4705473226"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705473227",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6771071,
          42.3479839
        ]
      },
      "id": "node/4705473227"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705473228",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6772935,
          42.345987
        ]
      },
      "id": "node/4705473228"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705473229",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6755272,
          42.3461674
        ]
      },
      "id": "node/4705473229"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705473230",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6743068,
          42.3461199
        ]
      },
      "id": "node/4705473230"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705473231",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6716166,
          42.3455202
        ]
      },
      "id": "node/4705473231"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705473232",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6756721,
          42.3455291
        ]
      },
      "id": "node/4705473232"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705473233",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6688877,
          42.3457132
        ]
      },
      "id": "node/4705473233"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705473234",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6767508,
          42.3444082
        ]
      },
      "id": "node/4705473234"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705473235",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.666796,
          42.3453566
        ]
      },
      "id": "node/4705473235"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705473236",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6700197,
          42.345983
        ]
      },
      "id": "node/4705473236"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705473238",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6662016,
          42.3462942
        ]
      },
      "id": "node/4705473238"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705473239",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6650268,
          42.3468612
        ]
      },
      "id": "node/4705473239"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4705473240",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6683335,
          42.3473626
        ]
      },
      "id": "node/4705473240"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883763",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6730404,
          42.3483042
        ]
      },
      "id": "node/4708883763"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883764",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6750921,
          42.3484402
        ]
      },
      "id": "node/4708883764"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883765",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6695988,
          42.3476915
        ]
      },
      "id": "node/4708883765"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883766",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6722033,
          42.348982
        ]
      },
      "id": "node/4708883766"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883767",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6708702,
          42.3496243
        ]
      },
      "id": "node/4708883767"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883768",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6698268,
          42.3496183
        ]
      },
      "id": "node/4708883768"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883769",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6683656,
          42.3496184
        ]
      },
      "id": "node/4708883769"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883770",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6685367,
          42.3480365
        ]
      },
      "id": "node/4708883770"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883771",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6675174,
          42.3474001
        ]
      },
      "id": "node/4708883771"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883772",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6670011,
          42.3492139
        ]
      },
      "id": "node/4708883772"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883773",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6671512,
          42.3499579
        ]
      },
      "id": "node/4708883773"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883774",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6682724,
          42.3506636
        ]
      },
      "id": "node/4708883774"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883775",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6699863,
          42.3506418
        ]
      },
      "id": "node/4708883775"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883776",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6701875,
          42.3514545
        ]
      },
      "id": "node/4708883776"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883777",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6686772,
          42.3523184
        ]
      },
      "id": "node/4708883777"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883778",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6690367,
          42.3509467
        ]
      },
      "id": "node/4708883778"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883779",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6724431,
          42.3513372
        ]
      },
      "id": "node/4708883779"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883780",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6693827,
          42.3530221
        ]
      },
      "id": "node/4708883780"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883781",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6674661,
          42.3515004
        ]
      },
      "id": "node/4708883781"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883782",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6663796,
          42.3476758
        ]
      },
      "id": "node/4708883782"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883783",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6667792,
          42.3496582
        ]
      },
      "id": "node/4708883783"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883784",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6658029,
          42.3499297
        ]
      },
      "id": "node/4708883784"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883785",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6637751,
          42.3501081
        ]
      },
      "id": "node/4708883785"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883786",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6621631,
          42.3489426
        ]
      },
      "id": "node/4708883786"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883787",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6620076,
          42.3505938
        ]
      },
      "id": "node/4708883787"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883890",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6628362,
          42.3505984
        ]
      },
      "id": "node/4708883890"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883891",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6650249,
          42.3502039
        ]
      },
      "id": "node/4708883891"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883892",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.666248,
          42.350971
        ]
      },
      "id": "node/4708883892"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883893",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6651278,
          42.3518848
        ]
      },
      "id": "node/4708883893"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883894",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6670873,
          42.3511314
        ]
      },
      "id": "node/4708883894"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883895",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6662837,
          42.3531535
        ]
      },
      "id": "node/4708883895"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883896",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.662554,
          42.3545178
        ]
      },
      "id": "node/4708883896"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883897",
        "amenity": "recycling",
        "location": "overground",
        "recycling:paper": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6617467,
          42.3531403
        ]
      },
      "id": "node/4708883897"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883899",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6642369,
          42.3547063
        ]
      },
      "id": "node/4708883899"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883900",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6645226,
          42.3548005
        ]
      },
      "id": "node/4708883900"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883901",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.671291,
          42.3524087
        ]
      },
      "id": "node/4708883901"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883902",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6749182,
          42.3528428
        ]
      },
      "id": "node/4708883902"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883903",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6757033,
          42.3520836
        ]
      },
      "id": "node/4708883903"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883904",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6750662,
          42.3519518
        ]
      },
      "id": "node/4708883904"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883905",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6716412,
          42.3536553
        ]
      },
      "id": "node/4708883905"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883906",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6709197,
          42.3545372
        ]
      },
      "id": "node/4708883906"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883907",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6748711,
          42.3537953
        ]
      },
      "id": "node/4708883907"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883908",
        "amenity": "recycling",
        "location": "overground",
        "recycling:beverage_cartons": "yes",
        "recycling:cans": "yes",
        "recycling:cardboard": "yes",
        "recycling:cartons": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic_bottles": "yes",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6752838,
          42.3562045
        ]
      },
      "id": "node/4708883908"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883909",
        "amenity": "recycling",
        "location": "overground",
        "recycling:beverage_cartons": "yes",
        "recycling:cans": "yes",
        "recycling:cardboard": "yes",
        "recycling:cartons": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic_bottles": "yes",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6764559,
          42.3564958
        ]
      },
      "id": "node/4708883909"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883910",
        "amenity": "recycling",
        "location": "overground",
        "recycling:beverage_cartons": "yes",
        "recycling:cans": "yes",
        "recycling:cardboard": "yes",
        "recycling:cartons": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic_bottles": "yes",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6733012,
          42.3569468
        ]
      },
      "id": "node/4708883910"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883911",
        "amenity": "recycling",
        "location": "overground",
        "recycling:beverage_cartons": "yes",
        "recycling:cans": "yes",
        "recycling:cardboard": "yes",
        "recycling:cartons": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic_bottles": "yes",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6716521,
          42.3562877
        ]
      },
      "id": "node/4708883911"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883912",
        "amenity": "recycling",
        "location": "overground",
        "recycling:beverage_cartons": "yes",
        "recycling:cans": "yes",
        "recycling:cardboard": "yes",
        "recycling:cartons": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic_bottles": "yes",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6705122,
          42.356922
        ]
      },
      "id": "node/4708883912"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883913",
        "amenity": "recycling",
        "location": "overground",
        "recycling:beverage_cartons": "yes",
        "recycling:cans": "yes",
        "recycling:cardboard": "yes",
        "recycling:cartons": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic_bottles": "yes",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6710218,
          42.3577524
        ]
      },
      "id": "node/4708883913"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883914",
        "amenity": "recycling",
        "location": "overground",
        "recycling:glass_bottles": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6694308,
          42.3559555
        ]
      },
      "id": "node/4708883914"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883915",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6687137,
          42.3549696
        ]
      },
      "id": "node/4708883915"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883916",
        "amenity": "recycling",
        "location": "overground",
        "recycling:beverage_cartons": "yes",
        "recycling:cans": "yes",
        "recycling:cardboard": "yes",
        "recycling:cartons": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic_bottles": "yes",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6680584,
          42.357634
        ]
      },
      "id": "node/4708883916"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883917",
        "amenity": "recycling",
        "location": "overground",
        "recycling:beverage_cartons": "yes",
        "recycling:cans": "yes",
        "recycling:cardboard": "yes",
        "recycling:cartons": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic_bottles": "yes",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6673832,
          42.3581891
        ]
      },
      "id": "node/4708883917"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883918",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6652992,
          42.3581663
        ]
      },
      "id": "node/4708883918"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883919",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6656099,
          42.355539
        ]
      },
      "id": "node/4708883919"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883920",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6672416,
          42.3551153
        ]
      },
      "id": "node/4708883920"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883921",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6652354,
          42.3565666
        ]
      },
      "id": "node/4708883921"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883922",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6666273,
          42.3567922
        ]
      },
      "id": "node/4708883922"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883923",
        "amenity": "recycling",
        "location": "overground",
        "recycling:beverage_cartons": "yes",
        "recycling:cans": "yes",
        "recycling:cardboard": "yes",
        "recycling:cartons": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic_bottles": "yes",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6681062,
          42.3562094
        ]
      },
      "id": "node/4708883923"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883924",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6635061,
          42.355994
        ]
      },
      "id": "node/4708883924"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883925",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6646875,
          42.3576804
        ]
      },
      "id": "node/4708883925"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883926",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6657751,
          42.3591094
        ]
      },
      "id": "node/4708883926"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883927",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6680361,
          42.3596451
        ]
      },
      "id": "node/4708883927"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883928",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6688569,
          42.3609413
        ]
      },
      "id": "node/4708883928"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883929",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6672835,
          42.361886
        ]
      },
      "id": "node/4708883929"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883930",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6660805,
          42.3625935
        ]
      },
      "id": "node/4708883930"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883931",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6640057,
          42.3625842
        ]
      },
      "id": "node/4708883931"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883932",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6653093,
          42.3610146
        ]
      },
      "id": "node/4708883932"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883933",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6622808,
          42.360119
        ]
      },
      "id": "node/4708883933"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883934",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6634287,
          42.3586867
        ]
      },
      "id": "node/4708883934"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883935",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6628601,
          42.3574063
        ]
      },
      "id": "node/4708883935"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883936",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6617818,
          42.3585588
        ]
      },
      "id": "node/4708883936"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883937",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6597447,
          42.3604595
        ]
      },
      "id": "node/4708883937"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883938",
        "amenity": "recycling",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6588246,
          42.3616226
        ]
      },
      "id": "node/4708883938"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883939",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6562072,
          42.3645463
        ]
      },
      "id": "node/4708883939"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883940",
        "amenity": "recycling",
        "location": "overground",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6543766,
          42.364205
        ]
      },
      "id": "node/4708883940"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883941",
        "amenity": "recycling",
        "location": "overground",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6536605,
          42.3633948
        ]
      },
      "id": "node/4708883941"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883942",
        "amenity": "recycling",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6545107,
          42.3632402
        ]
      },
      "id": "node/4708883942"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883943",
        "amenity": "recycling",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6558035,
          42.3634573
        ]
      },
      "id": "node/4708883943"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883944",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6554575,
          42.3627302
        ]
      },
      "id": "node/4708883944"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883945",
        "amenity": "recycling",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6551155,
          42.3620871
        ]
      },
      "id": "node/4708883945"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883946",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6523071,
          42.3601149
        ]
      },
      "id": "node/4708883946"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883947",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6515378,
          42.3642446
        ]
      },
      "id": "node/4708883947"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883948",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6517595,
          42.3626769
        ]
      },
      "id": "node/4708883948"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883949",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6476091,
          42.3618586
        ]
      },
      "id": "node/4708883949"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883950",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.650807,
          42.3577247
        ]
      },
      "id": "node/4708883950"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883951",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6605674,
          42.34768
        ]
      },
      "id": "node/4708883951"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883952",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6532374,
          42.3477072
        ]
      },
      "id": "node/4708883952"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883953",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6499213,
          42.3452059
        ]
      },
      "id": "node/4708883953"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883954",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6484088,
          42.3480925
        ]
      },
      "id": "node/4708883954"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883955",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6482211,
          42.3500381
        ]
      },
      "id": "node/4708883955"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883957",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6408978,
          42.3489956
        ]
      },
      "id": "node/4708883957"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883958",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6525022,
          42.344532
        ]
      },
      "id": "node/4708883958"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883959",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6499704,
          42.3436992
        ]
      },
      "id": "node/4708883959"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883960",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6465785,
          42.343033
        ]
      },
      "id": "node/4708883960"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883961",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.648559,
          42.3440038
        ]
      },
      "id": "node/4708883961"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883962",
        "amenity": "recycling",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6578748,
          42.3411246
        ]
      },
      "id": "node/4708883962"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883963",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6455965,
          42.3395094
        ]
      },
      "id": "node/4708883963"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883964",
        "amenity": "recycling",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6315623,
          42.3389032
        ]
      },
      "id": "node/4708883964"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883965",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6333138,
          42.3391441
        ]
      },
      "id": "node/4708883965"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883966",
        "amenity": "recycling",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6353778,
          42.3390489
        ]
      },
      "id": "node/4708883966"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883967",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6388714,
          42.3392927
        ]
      },
      "id": "node/4708883967"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883968",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6289194,
          42.3610779
        ]
      },
      "id": "node/4708883968"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883969",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6271447,
          42.3635076
        ]
      },
      "id": "node/4708883969"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883970",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.62898,
          42.3650869
        ]
      },
      "id": "node/4708883970"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883971",
        "amenity": "recycling",
        "recycling:glass_bottles": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6214898,
          42.3647856
        ]
      },
      "id": "node/4708883971"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883972",
        "amenity": "recycling",
        "recycling:glass_bottles": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6221589,
          42.3641153
        ]
      },
      "id": "node/4708883972"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883973",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6252545,
          42.3640407
        ]
      },
      "id": "node/4708883973"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883974",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6722208,
          42.3621845
        ]
      },
      "id": "node/4708883974"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883975",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6745283,
          42.3651245
        ]
      },
      "id": "node/4708883975"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883976",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6734501,
          42.3641653
        ]
      },
      "id": "node/4708883976"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883977",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6698772,
          42.3634495
        ]
      },
      "id": "node/4708883977"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883978",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6685567,
          42.3649373
        ]
      },
      "id": "node/4708883978"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883979",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6671522,
          42.3637571
        ]
      },
      "id": "node/4708883979"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883980",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6677839,
          42.3650175
        ]
      },
      "id": "node/4708883980"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883981",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6685081,
          42.3660292
        ]
      },
      "id": "node/4708883981"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883982",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6655079,
          42.3657137
        ]
      },
      "id": "node/4708883982"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883983",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6640622,
          42.3671307
        ]
      },
      "id": "node/4708883983"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883984",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6634894,
          42.3655537
        ]
      },
      "id": "node/4708883984"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883985",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6617512,
          42.3673547
        ]
      },
      "id": "node/4708883985"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883986",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6608164,
          42.3654968
        ]
      },
      "id": "node/4708883986"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883987",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6588812,
          42.3656524
        ]
      },
      "id": "node/4708883987"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883988",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6599899,
          42.3678583
        ]
      },
      "id": "node/4708883988"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883989",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6596962,
          42.3686074
        ]
      },
      "id": "node/4708883989"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883990",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6576738,
          42.3666702
        ]
      },
      "id": "node/4708883990"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883991",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6569013,
          42.3696725
        ]
      },
      "id": "node/4708883991"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883992",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6566908,
          42.3687788
        ]
      },
      "id": "node/4708883992"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883993",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6557802,
          42.3674302
        ]
      },
      "id": "node/4708883993"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883994",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6531266,
          42.3697767
        ]
      },
      "id": "node/4708883994"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883995",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6534951,
          42.3669822
        ]
      },
      "id": "node/4708883995"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883996",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6910364,
          42.3598172
        ]
      },
      "id": "node/4708883996"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883997",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6958283,
          42.3591984
        ]
      },
      "id": "node/4708883997"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883998",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7062085,
          42.356219
        ]
      },
      "id": "node/4708883998"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708883999",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7153485,
          42.3656283
        ]
      },
      "id": "node/4708883999"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4708884000",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7113852,
          42.3699513
        ]
      },
      "id": "node/4708884000"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4709938094",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7027547,
          42.3195989
        ]
      },
      "id": "node/4709938094"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4709938095",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7039214,
          42.3121271
        ]
      },
      "id": "node/4709938095"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4709938096",
        "amenity": "recycling",
        "mapillary": "895235347997910",
        "recycling_type": "container",
        "survey:date": "2019-01-09"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7589576,
          42.3596566
        ]
      },
      "id": "node/4709938096"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4709938097",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7593949,
          42.3641834
        ]
      },
      "id": "node/4709938097"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4709938098",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7513395,
          42.3668174
        ]
      },
      "id": "node/4709938098"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4709938099",
        "amenity": "recycling",
        "recycling:plastic": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7393165,
          42.3651275
        ]
      },
      "id": "node/4709938099"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4709938100",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7409165,
          42.368594
        ]
      },
      "id": "node/4709938100"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4709938101",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.744837,
          42.3679617
        ]
      },
      "id": "node/4709938101"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4709938102",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7375576,
          42.3749994
        ]
      },
      "id": "node/4709938102"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4709938103",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7351536,
          42.3695573
        ]
      },
      "id": "node/4709938103"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4709938104",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7293822,
          42.3700203
        ]
      },
      "id": "node/4709938104"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4709938105",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7297679,
          42.371513
        ]
      },
      "id": "node/4709938105"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4709938106",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7232037,
          42.3721921
        ]
      },
      "id": "node/4709938106"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4709938107",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7792417,
          42.3620501
        ]
      },
      "id": "node/4709938107"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4721035011",
        "amenity": "recycling",
        "location": "overground",
        "recycling:glass_bottles": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7124564,
          42.3454672
        ]
      },
      "id": "node/4721035011"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4747560530",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.715502,
          42.3720176
        ]
      },
      "id": "node/4747560530"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4747560531",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6321738,
          42.3632648
        ]
      },
      "id": "node/4747560531"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4751469940",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6198,
          42.342873
        ]
      },
      "id": "node/4751469940"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4751469941",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6417485,
          42.3588667
        ]
      },
      "id": "node/4751469941"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4751469942",
        "amenity": "recycling",
        "recycling:paper": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7193019,
          42.371779
        ]
      },
      "id": "node/4751469942"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4758248435",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7142296,
          42.3463366
        ]
      },
      "id": "node/4758248435"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4758248444",
        "amenity": "recycling",
        "recycling:glass_bottles": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7351398,
          42.3697776
        ]
      },
      "id": "node/4758248444"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4758248445",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.635356,
          42.3597823
        ]
      },
      "id": "node/4758248445"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4760495930",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7115387,
          42.3472938
        ]
      },
      "id": "node/4760495930"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4779682995",
        "amenity": "recycling",
        "recycling:glass_bottles": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7335164,
          42.370956
        ]
      },
      "id": "node/4779682995"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4779682996",
        "amenity": "recycling",
        "recycling:glass_bottles": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7237586,
          42.3750815
        ]
      },
      "id": "node/4779682996"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4779682997",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7230303,
          42.3743102
        ]
      },
      "id": "node/4779682997"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4779682998",
        "amenity": "recycling",
        "recycling:glass_bottles": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7113426,
          42.3643063
        ]
      },
      "id": "node/4779682998"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4781887223",
        "amenity": "recycling",
        "location": "overground",
        "recycling:paper": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6611768,
          42.3520066
        ]
      },
      "id": "node/4781887223"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4818718164",
        "amenity": "recycling",
        "operator": "Cáritas",
        "recycling:clothes": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7154537,
          42.3457207
        ]
      },
      "id": "node/4818718164"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/4904544802",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6226293,
          42.3558898
        ]
      },
      "id": "node/4904544802"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/5031101128",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7177044,
          42.3468728
        ]
      },
      "id": "node/5031101128"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/5279312116",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6949244,
          42.3314648
        ]
      },
      "id": "node/5279312116"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/5292402433",
        "amenity": "recycling",
        "recycling:glass_bottles": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6917425,
          42.3759604
        ]
      },
      "id": "node/5292402433"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/5331025104",
        "amenity": "recycling",
        "check_date:recycling": "2020-12-29",
        "operator": "Urbaser",
        "recycling:glass_bottles": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6975534,
          42.3348321
        ]
      },
      "id": "node/5331025104"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/5331965977",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7062978,
          42.3329718
        ]
      },
      "id": "node/5331965977"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/5335726950",
        "amenity": "recycling",
        "location": "overground",
        "operator": "Cáritas",
        "recycling:clothes": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.713261,
          42.3414904
        ]
      },
      "id": "node/5335726950"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/5410290303",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7218998,
          42.3405695
        ]
      },
      "id": "node/5410290303"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/5415278979",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7335651,
          42.3437188
        ]
      },
      "id": "node/5415278979"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/5415278985",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7335511,
          42.343218
        ]
      },
      "id": "node/5415278985"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/5429741872",
        "amenity": "recycling",
        "location": "overground",
        "operator": "Fundación Lesmes",
        "recycling:clothes": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7309809,
          42.3414052
        ]
      },
      "id": "node/5429741872"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/5476261884",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7042326,
          42.3433364
        ]
      },
      "id": "node/5476261884"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/5491050387",
        "amenity": "recycling",
        "check_date:recycling": "2021-03-14",
        "location": "overground",
        "recycling:glass_bottles": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7084778,
          42.3426545
        ]
      },
      "id": "node/5491050387"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/5501186699",
        "amenity": "recycling",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7174255,
          42.342738
        ]
      },
      "id": "node/5501186699"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/5540997060",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7060172,
          42.3296662
        ]
      },
      "id": "node/5540997060"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/5542737813",
        "amenity": "recycling",
        "location": "overground",
        "operator": "Cáritas",
        "recycling:clothes": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7040556,
          42.3318984
        ]
      },
      "id": "node/5542737813"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/5581000718",
        "amenity": "recycling",
        "ele": "-1",
        "location": "overground",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6987595,
          42.3431053
        ]
      },
      "id": "node/5581000718"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/5596929485",
        "amenity": "recycling",
        "location": "overground",
        "operator": "Cáritas Diocesana",
        "recycling:clothes": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6918149,
          42.351913
        ]
      },
      "id": "node/5596929485"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/5602495414",
        "amenity": "recycling",
        "location": "overground",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7008283,
          42.3439582
        ]
      },
      "id": "node/5602495414"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/5609694090",
        "amenity": "recycling",
        "operator": "Fundación Lesmes",
        "recycling:clothes": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7208789,
          42.3464502
        ]
      },
      "id": "node/5609694090"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/5864145871",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6660818,
          42.3273361
        ]
      },
      "id": "node/5864145871"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/6069211660",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6291621,
          42.337804
        ]
      },
      "id": "node/6069211660"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/6069211676",
        "amenity": "recycling",
        "recycling:glass_bottles": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6332629,
          42.3390251
        ]
      },
      "id": "node/6069211676"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/6138082171",
        "amenity": "recycling",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6635456,
          42.3405084
        ]
      },
      "id": "node/6138082171"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/6227118507",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6534678,
          42.3464395
        ]
      },
      "id": "node/6227118507"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/6236868409",
        "amenity": "recycling",
        "recycling:clothes": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.648222,
          42.3446814
        ]
      },
      "id": "node/6236868409"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/6262623767",
        "amenity": "recycling",
        "recycling:glass_bottles": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.622042,
          42.3632862
        ]
      },
      "id": "node/6262623767"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/6270024749",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6150849,
          42.3661257
        ]
      },
      "id": "node/6270024749"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/6297692016",
        "amenity": "recycling",
        "recycling:cans": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7075384,
          42.3346997
        ]
      },
      "id": "node/6297692016"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/6319726288",
        "amenity": "recycling",
        "recycling:clothes": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6752034,
          42.3617058
        ]
      },
      "id": "node/6319726288"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/6340325760",
        "amenity": "recycling",
        "recycling:glass_bottles": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7104266,
          42.3611015
        ]
      },
      "id": "node/6340325760"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/6770475774",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.701463,
          42.3007826
        ]
      },
      "id": "node/6770475774"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/6770475776",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7017535,
          42.2972094
        ]
      },
      "id": "node/6770475776"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/6786541614",
        "amenity": "recycling",
        "location": "overground",
        "recycling:paper": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6584143,
          42.3519068
        ]
      },
      "id": "node/6786541614"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/6786541615",
        "amenity": "recycling",
        "location": "overground",
        "recycling:plastic": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6585078,
          42.3540307
        ]
      },
      "id": "node/6786541615"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/6786541616",
        "amenity": "recycling",
        "location": "overground",
        "recycling:paper": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6602271,
          42.3535649
        ]
      },
      "id": "node/6786541616"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/6786541617",
        "amenity": "recycling",
        "location": "overground",
        "recycling:paper": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6608443,
          42.353253
        ]
      },
      "id": "node/6786541617"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/6786541618",
        "amenity": "recycling",
        "location": "overground",
        "recycling:paper": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6623199,
          42.3551059
        ]
      },
      "id": "node/6786541618"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/6820903770",
        "amenity": "recycling",
        "location": "overground",
        "recycling:glass_bottles": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6566315,
          42.3566632
        ]
      },
      "id": "node/6820903770"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/7170316076",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6968468,
          42.3761994
        ]
      },
      "id": "node/7170316076"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/7176120632",
        "amenity": "recycling",
        "recycling:clothes": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6858512,
          42.3526637
        ]
      },
      "id": "node/7176120632"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/7182195904",
        "amenity": "recycling",
        "location": "overground",
        "recycling:beverage_cartons": "yes",
        "recycling:cans": "yes",
        "recycling:cardboard": "yes",
        "recycling:cartons": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic_bottles": "yes",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6849127,
          42.3537859
        ]
      },
      "id": "node/7182195904"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/7214734222",
        "amenity": "recycling",
        "recycling:glass_bottles": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6872697,
          42.3600162
        ]
      },
      "id": "node/7214734222"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/7253642873",
        "amenity": "recycling",
        "location": "overground",
        "recycling:beverage_cartons": "yes",
        "recycling:cans": "yes",
        "recycling:cardboard": "yes",
        "recycling:cartons": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:organic": "yes",
        "recycling:paper": "yes",
        "recycling:plastic_bottles": "yes",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6763855,
          42.358145
        ]
      },
      "id": "node/7253642873"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/7978229611",
        "amenity": "recycling",
        "recycling:clothes": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7248288,
          42.3363702
        ]
      },
      "id": "node/7978229611"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/7982064721",
        "amenity": "recycling",
        "recycling:clothes": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6758992,
          42.346281
        ]
      },
      "id": "node/7982064721"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/8010734556",
        "amenity": "recycling",
        "recycling:waste": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6630084,
          42.3399945
        ]
      },
      "id": "node/8010734556"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/8010734605",
        "amenity": "recycling",
        "recycling:waste": "no",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6524505,
          42.3396694
        ]
      },
      "id": "node/8010734605"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/8089352758",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6814341,
          42.3490143
        ]
      },
      "id": "node/8089352758"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/8567421861",
        "amenity": "recycling",
        "operator": "Fundación Lesmes",
        "recycling:clothes": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7027031,
          42.3357609
        ]
      },
      "id": "node/8567421861"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/8607466993",
        "amenity": "recycling",
        "recycling:clothes": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6564602,
          42.3632552
        ]
      },
      "id": "node/8607466993"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/8951929486",
        "amenity": "recycling",
        "location": "overground",
        "recycling:beverage_cartons": "yes",
        "recycling:cans": "yes",
        "recycling:cardboard": "yes",
        "recycling:cartons": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic_bottles": "yes",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6848209,
          42.3547689
        ]
      },
      "id": "node/8951929486"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/9045554771",
        "amenity": "recycling",
        "recycling:cooking_oil": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6773483,
          42.355029
        ]
      },
      "id": "node/9045554771"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/9045554772",
        "amenity": "recycling",
        "recycling:cooking_oil": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6681027,
          42.3576197
        ]
      },
      "id": "node/9045554772"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/9045554773",
        "amenity": "recycling",
        "recycling:clothes": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6728693,
          42.3569162
        ]
      },
      "id": "node/9045554773"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/9045554774",
        "amenity": "recycling",
        "recycling:clothes": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.667562,
          42.3585296
        ]
      },
      "id": "node/9045554774"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/9051724733",
        "amenity": "recycling",
        "recycling:cooking_oil": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6751744,
          42.3617217
        ]
      },
      "id": "node/9051724733"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/9051724734",
        "amenity": "recycling",
        "recycling:clothes": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.679698,
          42.3593956
        ]
      },
      "id": "node/9051724734"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/9051724735",
        "amenity": "recycling",
        "recycling:cooking_oil": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6798133,
          42.3594301
        ]
      },
      "id": "node/9051724735"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/9058994751",
        "amenity": "recycling",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_packaging": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7021936,
          42.3444031
        ]
      },
      "id": "node/9058994751"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/9200871463",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7052504,
          42.3575342
        ]
      },
      "id": "node/9200871463"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/9220972021",
        "amenity": "recycling",
        "recycling:green_waste": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7309345,
          42.3424217
        ]
      },
      "id": "node/9220972021"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/9434365848",
        "amenity": "recycling",
        "recycling:clothes": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7126698,
          42.3337293
        ]
      },
      "id": "node/9434365848"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/9598129791",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6614281,
          42.3478959
        ]
      },
      "id": "node/9598129791"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/9741859300",
        "amenity": "recycling",
        "recycling:beverage_cartons": "yes",
        "recycling:cans": "yes",
        "recycling:glass_bottles": "yes",
        "recycling:paper": "yes",
        "recycling:plastic": "no",
        "recycling:plastic_bottles": "yes",
        "recycling:plastic_packaging": "no",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7007109,
          42.3383068
        ]
      },
      "id": "node/9741859300"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/9770442339",
        "amenity": "recycling",
        "recycling:glass_bottles": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6970771,
          42.3495281
        ]
      },
      "id": "node/9770442339"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/9801407055",
        "amenity": "recycling",
        "recycling:oil": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6975884,
          42.3486977
        ]
      },
      "id": "node/9801407055"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/10013674776",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7237579,
          42.3384995
        ]
      },
      "id": "node/10013674776"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/10013674777",
        "amenity": "recycling",
        "recycling:plastic": "yes",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7250176,
          42.3365509
        ]
      },
      "id": "node/10013674777"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/10073745583",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7295529,
          42.3392534
        ]
      },
      "id": "node/10073745583"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/10141299284",
        "amenity": "recycling",
        "location": "overground",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6619744,
          42.3521358
        ]
      },
      "id": "node/10141299284"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/10189187967",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.7178838,
          42.3344261
        ]
      },
      "id": "node/10189187967"
    },
    {
      "type": "Feature",
      "properties": {
        "@id": "node/10232737112",
        "amenity": "recycling",
        "recycling_type": "container"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -3.6995323,
          42.3344917
        ]
      },
      "id": "node/10232737112"
    }
  ]
}
resultado={}
for element in data["features"]:
    LatLng=element["geometry"]["coordinates"]
    #LatLng[0]+=1
    LatLng.reverse()
    print(LatLng)