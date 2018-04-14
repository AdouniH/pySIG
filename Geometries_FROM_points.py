# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 14:47:57 2018

@author: houssem
"""
import fiona
from shapely.geometry import Polygon,mapping,MultiPoint
from fiona.crs import from_epsg
from shapely import affinity

class ensemble_points:
    def __init__(self,*points):
        self.points=points
    def polygon_contenant(self):
        polygon = Polygon(self.points)
        return polygon 
    def enveloppe_convexe(self):
        multipt=MultiPoint(self.points)
        return (multipt.convex_hull)
    def bounding_box(self):
        multipt=MultiPoint(self.points)
        a=multipt.bounds
        p1=(a[0],a[1])
        p2=(a[0],a[3])
        p3=(a[2],a[3])
        p4=(a[2],a[1])
        return Polygon([p1,p2,p3,p4])
    def minimum_oriented_boundingbox(self):
        p=self.enveloppe_convexe()
        m_bb=self.bounding_box().area
        k=0
        for i in range(360):
            rotated_b = affinity.rotate(p, i, origin='centroid')
            a=rotated_b.bounds
            p1=(a[0],a[1])
            p2=(a[0],a[3])
            p3=(a[2],a[3])
            p4=(a[2],a[1])
            m_cc=Polygon([p1,p2,p3,p4]).area
            pp=Polygon([p1,p2,p3,p4])
            if m_cc<m_bb:
                m_bb=m_cc
                polygon_retenu=pp
                k=i
        vrai_poly=affinity.rotate(polygon_retenu, -k, origin='centroid')
        return Polygon(vrai_poly)    
    def exporter(self,**information):
        # i think its better use design pattern strategy here ! :p  
        if information["type_enveloppe"]=="convex_hull":
            a=self.enveloppe_convexe()
        elif information["type_enveloppe"]=="polygon":
            a=self.polygon_contenant()
        elif information["type_enveloppe"]=="bounding_box":
            a=self.bounding_box()
        elif information["type_enveloppe"]=="min_oriented_box":
            a=self.minimum_oriented_boundingbox()
        schema = { 'geometry': 'Polygon', 'properties': { 'id': 'int'} }
        with fiona.open("/home/houssem/Bureau/hi.shp", "w", information["type_export"], schema, crs=from_epsg(4326)) as output:
            output.write({'properties': {'id' : 0},'geometry': mapping(a)})
            

if __name__ == "__main__":
    c=ensemble_points((0.45,0.540),(3.64,-1.4),(5.5,6.3),(1.3,3.3),(0.47,2.09),(0.69,2.35),(2.15,1.63))
    c.exporter(type_enveloppe="min_oriented_box",type_export="ESRI Shapefile")


