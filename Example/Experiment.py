#!/usr/bin/env python

###
### This file is generated automatically by SALOME v9.2.1 with dump python functionality
###


# Import SALOME module

import sys

import salome

import numpy as np

salome.salome_init()


# Import SALOME notebook

import salome_notebook

notebook = salome_notebook.NoteBook()



# Import NyRTex module

####################################
# IMPORTANT: NyRTex package location
####################################

# sys.path.append(r'/users/fogliate/.local/lib/python3.5/site-packages/nyrtex_path/')
sys.path.append(r'C:path\to\nyrtex_path')

import nyrtex_path as nt



# Import SALOME geometry module

import GEOM

from salome.geom import geomBuilder

import math

import SALOMEDS

geompy = geomBuilder.New()



# Create Engin-X Experiment

enginx = nt.EnginXExp(geompy, pub_det=False, pub_lines=False, Nx = 2, Nz = 5)



# Rotations

rotations = [(0,0,0), (30,45,0)]


# Cylindrical sample

baseSample = nt.cylSample(geompy, enginx, 0.015, 0.05)

samples = []

for rot in rotations:

  samples.append( baseSample.Rot1(geompy, enginx, rot) )


  

# Add to study (only for visualization)

for rot,sample in zip(rotations,samples):

  geompy.addToStudy(sample.Sample, sample.name + '_{}_{}_{}'.format(rot[0],rot[1], rot[2]))



  
# Compute paths

paths_list = []

for rot,sample in zip(rotations,samples):

  paths, beam = enginx.flight_distance( geompy, sample.Sample, show=True, name = sample.name + '_{}_{}_{}'.format(rot[0],rot[1], rot[2]) )
  
  if not paths_list:

    paths_list = paths

  else:

    paths_list = np.column_stack( (paths_list, paths) )



    
# Write paths

with open('Sample_fp.dat','w') as f:

  for rot in paths_list:

    for r in rot:

      f.write('{:.7g} '.format(r))

    f.write('\n')

    

    

if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
