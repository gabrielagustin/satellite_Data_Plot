# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 20:16:04 2018

@author: gag

"""

import os
import geopandas as gpd
import functions
import matplotlib.pyplot as plt

# from geopy.distance import distance



if __name__ == "__main__":

    # If a certain environment variable is set, look there for the input
    # file, otherwise look in the current directory.
    hdfFile = '/home/gag/Escritorio/SMAP_L1B/SMAP_L1B_TB_20137_A_20181108T101842_R16020_001.h5'
    # hdfFile = '/home/gag/Escritorio/SMAP_L1B/SMAP_L1B_TB_00884_D_20150402T002943_R16010_001.h5'
    try:
        hdfFile = os.path.join(os.environ['HDFEOS_ZOO_DIR'], hdffile)
    except KeyError:
        pass
    ##### lee el archivo HDF, se extrae la variable y se genera el objeto geopandas
    nameVariable = ['/Brightness_Temperature/tb_h']
    # pdHDF = functions.readHDF(hdfFile, nameVariable)
    box_lat = [-85, -65]
    box_lon = [120, 180]
    pdHDF = functions.read_SMAP_L1B_HDF_box(hdfFile, box_lat, box_lon, nameVariable)

    gdfHDF = gpd.GeoDataFrame(pdHDF, geometry='Coordinates')
    # # print(gdfHDF)


    ##### lee el archivo KML y se crea un objeto geopandas
    kmlFile = "/home/gag/Escritorio/Lineas_de_vuelo_Antartida/2018_UWBRAD_flight_1.kml"
    pdKML = functions.readKML(kmlFile)
    gdfKML = gpd.GeoDataFrame(pdKML, geometry='Coordinates')

    # # # # # Finally, we plot the coordinates over a country-level map.
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

    # # # We restrict to South America.
    ax = world[world.continent == 'Antarctica'].plot(
        color='white', edgecolor='black')

    
    
    gdfHDF.plot(ax=ax, cmap=plt.cm.jet)
    gdfKML.plot(ax=ax, color='red')
    
    plt.show()

