# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 22:12:05 2018

@author: houssem
"""

# convert file to another format 

import fiona 
def convert(input_file,output_driver_name):
    with fiona.open(input_file, 'r') as source:
        with fiona.open('name_of_output_file', 'w',crs=source.crs,driver=output_driver_name,schema=source.schema) as output:
            for line in source:
                output.write(line)
                
#convertir shapefile --> mapinfo file :
convert('output_files_test/output2.shp','MapInfo File')

