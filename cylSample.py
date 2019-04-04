import salome

import numpy as np

import EnginXExp as ngx


def cylSample(geompy, enginx, radius, height, name='Sample'):

    """

    Cylindrical sample

    """


    # Create simple cylinder
    
    Vertex_Sample = geompy.MakeVertex(0, 0, 0)
    
    Sample = geompy.MakeCylinder(Vertex_Sample, enginx.OZ, radius, height)


    
    # Translate cylinder: COM matches enginx origin

    COM = geompy.MakeCDG(Sample)

    vec = geompy.MakeVector(COM, enginx.O)

    Sample = geompy.MakeTranslationVector(Sample,vec)
    
    geompy.addToStudy( Sample, name )
    
    
    return Sample
