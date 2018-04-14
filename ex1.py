# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 21:45:21 2018
@author: houssem
"""

from fiona.crs import from_epsg
import fiona 
from shapely.geometry import Point,Polygon, mapping
import csv

        

schemaw={'geometry': 'Point','properties': {'id': 'int','categorie': 'str'}}

with fiona.open('output_files_test/output.shp', 'w',driver='ESRI Shapefile',crs=from_epsg(27561), schema=schemaw) as output:
    with open('data/points_EPSG-27561.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        j=0
        for row in reader:
            j+=1
            east=row['Easting']
            east=east.replace(",", ".")
            north=row['Northing']
            north=north.replace(",", ".")
            print(row['Group'],north, east)
            if row['Group'][-1]=="1":
                category='a'
            elif row['Group'][-1]=="2":
                category='b'
            elif row['Group'][-1]=="3":
                category='c'
            point = Point(float(north),float(east),2)
            output.write({'properties': {'id': j,'categorie': category},'geometry': mapping(point)})
        
   
schemawPolygon={'geometry': 'Polygon','properties': {'id': 'int','categorie': 'str'}}
with fiona.open('output_files_test/output2.shp', 'w',driver='ESRI Shapefile',crs=from_epsg(27561), schema=schemawPolygon) as output_polygones:
    with fiona.open('output_files_test/output.shp', 'r') as input_shp:
        poly1=[]        
        poly2=[] 
        poly3=[] 
        for line in input_shp:
            if line["properties"]["categorie"]=='a':
                poly1.append(line["geometry"]["coordinates"])
        polygon_1 = Polygon(poly1) 
        output_polygones.write({'properties': {'id': 0,'categorie': 'a'},'geometry': mapping(polygon_1.convex_hull.buffer(1.0))})
        for line in input_shp:
            if line["properties"]["categorie"]=='b':
                poly2.append(line["geometry"]["coordinates"])
        polygon_2 = Polygon(poly2) 
        output_polygones.write({'properties': {'id': 1,'categorie': 'b'},'geometry': mapping(polygon_2.convex_hull.buffer(1.0))})
        for line in input_shp:
            if line["properties"]["categorie"]=='c':
                poly3.append(line["geometry"]["coordinates"])
        polygon_3 = Polygon(poly3) 
        output_polygones.write({'properties': {'id': 2,'categorie': 'c'},'geometry': mapping(polygon_3.convex_hull.buffer(1.0))})
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        