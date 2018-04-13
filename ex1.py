# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 21:45:21 2018

@author: houssem
"""

from fiona.crs import from_epsg
import fiona 

shemaw={'geometry': 'Point','properties': {'id': 'int','categorie': 'str'}}

with fiona.open('/home/houssem/postedetravail/pythonSIG/p/pySIG/output.shp', 'w',driver=source_driver,crs=from_epsg(3857), schema=source_schema) as source:
    