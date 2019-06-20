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

sys.path.append(r'/home/ezequiel/.local/lib/python3.5/site-packages/nyrtex_path/')

import nyrtex_path as nt



# Import SALOME geometry module

import GEOM

from salome.geom import geomBuilder

import math

import SALOMEDS

geompy = geomBuilder.New()



# Create Engin-X Experiment

enginx = nt.EnginXExp(geompy, pub_det=False, pub_lines=False, Nx = 2, Nz = 5)


# Traslations

traslations = [(0,0,0), (0, 0.009, 0), (0,-0.009,0), (-0.009, 0, 0)]


# Rotations

rotations = [ (0.00 ,  0.00   ,  0.00), 
              (0.00 ,  30.00  ,  0.00), 
              (0.00 , -30.00  ,  0.00),
              (15.00,  45.00  ,  0.00),
              (15.00,  15.00  ,  0.00), 
              (15.00,  -15.00 ,  0.00),
              (45.00,  0.00   ,  0.00),
              (45.00,  30.00  ,  0.00),
              (45.00,  -30.00 ,  0.00),
              (60.00,  15.00  ,  0.00),
              (60.00,  -15.00 ,  0.00),
              (60.00,  -45.00 ,  0.00),
              (90.00,  -15.00 ,  0.00), 
              (90.00,  -30.00 ,  0.00),  
              (90.00,  15.00  ,  0.00),  
              (90.00,  30.00  ,  0.00),  
              (90.00,  45.00  ,  0.00) ]
 


# Iterate over traslations

for i,t in enumerate(traslations):

 
  # Cylindrical sample

  baseSample = nt.cylSample(geompy, enginx, 0.01375, 0.180, X0=t[0], Y0=t[1], Z0=t[2], name='M15')


  samples = []

  for rot in rotations:

    samples.append( baseSample.Rot1(geompy, enginx, rot) )


  # Add to study (only for visualization)

  for rot,sample in zip(rotations,samples):

    geompy.addToStudy(sample.Sample, sample.name + '_{}_{}_{}'.format(rot[0], rot[1], rot[2]))



 
  # Compute paths

  paths_list = []

  for rot,sample in zip(rotations,samples):

    paths, beam = enginx.flight_distance( geompy, sample.Sample, show=True, name = sample.name + '_{}_{}_{}'.format(rot[0],rot[1], rot[2]) )
  
    paths_list.append( [x + beam for x in paths] )


    
    
  # Write paths

  with open(sample.name + '_fp_{}.dat'.format(i),'w') as f:

    for det in range(len(paths_list[0])):

      for rot in range(len(paths_list)):

        f.write('{:.7g} '.format(paths_list[rot][det]))

      f.write('\n')

    

    

if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
