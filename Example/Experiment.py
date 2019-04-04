# -*- coding: utf-8 -*-

###
### This file is generated automatically by SALOME v8.2.0 with dump python functionality
###


# Import SALOME module

import sys

import salome

salome.salome_init()

theStudy = salome.myStudy



# Import SALOME notebook

import salome_notebook

notebook = salome_notebook.NoteBook(theStudy)

sys.path.insert( 0, r'/users/fogliate/.local/lib/python3.5/site-packages')



# Import NyRTex module

import nyrtex_path as nt



# Import SALOME geometry module

import GEOM

from salome.geom import geomBuilder

import math

import SALOMEDS

geompy = geomBuilder.New(theStudy)





# Create Engin-X Experiment

enginx = nt.EnginXExp(geompy, pub_det=False, pub_lines=False)


# Cylindrical sample

sample = nt.cylSample(geompy, enginx, 0.015, 0.05)



if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser(True)
