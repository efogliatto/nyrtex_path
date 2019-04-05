import salome

import numpy as np

from copy import deepcopy

from .EnginXExp import EnginXExp as ngx


class cylSample: 

    """

    Cylindrical sample.
    Principal axis in Z-direction

    """

    def __init__(self, geompy, enginx, radius, height, name='Sample', X0 = 0, Y0 = 0, Z0 = 0):
    

        """

        Constructor
        Arguments:

        X0: Center of mass translation in X direction
        Y0: Center of mass translation in Y direction
        Z0: Center of mass translation in Z direction

        """

        self.name = name

        
        # Create simple cylinder
    
        Vertex_Sample = geompy.MakeVertex(0, 0, 0)
    
        self.Sample = geompy.MakeCylinder(Vertex_Sample, enginx.OZ, radius, height)


    
        # Translate cylinder: COM matches enginx origin

        COM = geompy.MakeCDG(self.Sample)

        vec = geompy.MakeVector(COM, enginx.O)

        self.Sample = geompy.MakeTranslationVector(self.Sample,vec)

        self.COM = geompy.MakeCDG(self.Sample)        
    
        # geompy.addToStudy( self.Sample, name )


        
        # Local coordinate system
        
        self.OX = geompy.MakeVectorDXDYDZ(2.*radius, 0, 0)

        self.OY = geompy.MakeVectorDXDYDZ(0, 2.*radius, 0)

        self.OZ = geompy.MakeVectorDXDYDZ(0, 0, height)



        # Translate everything

        self.Sample = geompy.MakeTranslation(self.Sample, X0, Y0, Z0)

        self.OX = geompy.MakeTranslation(self.OX, X0, Y0, Z0)

        self.OY = geompy.MakeTranslation(self.OY, X0, Y0, Z0)

        self.OZ = geompy.MakeTranslation(self.OZ, X0, Y0, Z0)
        
        
    
        pass







    def Rot1(self, geompy, enginx, rot=(0,0,0)):

        
        """

        Rot1 type rotations

        """


        # Chi rotation

        newSample = deepcopy(self)
        
        newSample.Sample = geompy.MakeRotation(self.Sample, enginx.OY, rot[0])

        newSample.OX = geompy.MakeRotation(self.OX, enginx.OY, rot[0])

        newSample.OY = geompy.MakeRotation(self.OY, enginx.OY, rot[0])

        newSample.OZ = geompy.MakeRotation(self.OY, enginx.OY, rot[0])        



        # Omega rotation
        
        newSample.Sample = geompy.MakeRotation(newSample.Sample, enginx.OZ, rot[1])

        newSample.OX = geompy.MakeRotation(newSample.OX, enginx.OZ, rot[1])

        newSample.OY = geompy.MakeRotation(newSample.OY, enginx.OZ, rot[1])

        newSample.OZ = geompy.MakeRotation(newSample.OY, enginx.OZ, rot[1])



        # Phi rotation
        
        newSample.Sample = geompy.MakeRotation(newSample.Sample, newSample.OZ, rot[2])

        newSample.OX = geompy.MakeRotation(newSample.OX, newSample.OZ, rot[2])

        newSample.OY = geompy.MakeRotation(newSample.OY, newSample.OZ, rot[2])



        return newSample



    


    def EulerRot(self, geompy, enginx, rot=(0,0,0)):

        
        """

        Euler-type rotations

        """


        # Alpha rotation

        newSample = deepcopy(self)        
        
        newSample.Sample = geompy.MakeRotation(self.Sample, enginx.OZ, rot[0])

        newSample.OX = geompy.MakeRotation(self.OX, enginx.OZ, rot[0])

        newSample.OY = geompy.MakeRotation(self.OY, enginx.OZ, rot[0])

        newSample.OZ = geompy.MakeRotation(self.OY, enginx.OZ, rot[0])        



        # Beta rotation
        
        newSample.Sample = geompy.MakeRotation(newSample.Sample, newSample.OX, rot[1])

        newSample.OY = geompy.MakeRotation(newSample.OY, newSample.OX, rot[1])

        newSample.OZ = geompy.MakeRotation(newSample.OY, newSample.OX, rot[1])



        # Gamma rotation
        
        newSample.Sample = geompy.MakeRotation(newSample.Sample, newSample.OZ, rot[2])

        newSample.OX = geompy.MakeRotation(newSample.OX, newSample.OZ, rot[2])

        newSample.OY = geompy.MakeRotation(newSample.OY, newSample.OZ, rot[2])



        return newSample    
