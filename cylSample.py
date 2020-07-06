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
    


        
        # Local coordinate system
        
        self.OX = geompy.MakeVectorDXDYDZ(2.*radius, 0, 0)

        self.OY = geompy.MakeVectorDXDYDZ(0, 2.*radius, 0)

        self.OZ = geompy.MakeVectorDXDYDZ(0, 0, height)



        # Initial traslation

        self.Sample = geompy.MakeTranslation(self.Sample, X0, Y0, Z0)




        # Save translations

        self.initTras = [X0, Y0, Z0]

        
        # Save rotations
        
        self.initRot = [0,0,0]
        
        
    
        pass







    def Rot_YZZp(self, geompy, enginx, rot=(0,0,0)):

        
        """

        Rotation type:
        X, Z, Z'

        """


        degree = [x*np.pi/180.0 for x in rot]

        self.initRot = degree

        

        # Chi rotation

        newSample = deepcopy(self)
        
        newSample.Sample = geompy.MakeRotation(self.Sample, enginx.OY, degree[0])

        newSample.OX = geompy.MakeRotation(self.OX, enginx.OY, degree[0])

        newSample.OY = geompy.MakeRotation(self.OY, enginx.OY, degree[0])

        newSample.OZ = geompy.MakeRotation(self.OZ, enginx.OY, degree[0])        



        # Omega rotation
        
        newSample.Sample = geompy.MakeRotation(newSample.Sample, enginx.OZ, degree[1])

        newSample.OX = geompy.MakeRotation(newSample.OX, enginx.OZ, degree[1])

        newSample.OY = geompy.MakeRotation(newSample.OY, enginx.OZ, degree[1])

        newSample.OZ = geompy.MakeRotation(newSample.OZ, enginx.OZ, degree[1])



        # Phi rotation
        
        newSample.Sample = geompy.MakeRotation(newSample.Sample, newSample.OZ, degree[2])

        newSample.OX = geompy.MakeRotation(newSample.OX, newSample.OZ, degree[2])

        newSample.OY = geompy.MakeRotation(newSample.OY, newSample.OZ, degree[2])




        return newSample





    def Rot_XZZp(self, geompy, enginx, rot=(0,0,0)):

        
        """

        Rotation type:
        X, Z, Z'

        """


        degree = [x*np.pi/180.0 for x in rot]

        self.initRot = degree

        

        # Chi rotation

        newSample = deepcopy(self)
        
        newSample.Sample = geompy.MakeRotation(self.Sample, enginx.OX, degree[0])

        newSample.OX = geompy.MakeRotation(self.OX, enginx.OX, degree[0])

        newSample.OY = geompy.MakeRotation(self.OY, enginx.OX, degree[0])

        newSample.OZ = geompy.MakeRotation(self.OZ, enginx.OX, degree[0])        



        # Omega rotation
        
        newSample.Sample = geompy.MakeRotation(newSample.Sample, enginx.OZ, degree[1])

        newSample.OX = geompy.MakeRotation(newSample.OX, enginx.OZ, degree[1])

        newSample.OY = geompy.MakeRotation(newSample.OY, enginx.OZ, degree[1])

        newSample.OZ = geompy.MakeRotation(newSample.OZ, enginx.OZ, degree[1])



        # Phi rotation
        
        newSample.Sample = geompy.MakeRotation(newSample.Sample, newSample.OZ, degree[2])

        newSample.OX = geompy.MakeRotation(newSample.OX, newSample.OZ, degree[2])

        newSample.OY = geompy.MakeRotation(newSample.OY, newSample.OZ, degree[2])




        return newSample

    




    def Gauge_Rot1(self, geompy, enginx, vol=(0.004,0.004,0.006)):

        
        """

        Rot1 type rotations

        """


        # Gauge volume
        
        gv0 = geompy.MakeVertex(-vol[0]/2, -vol[1]/2, -vol[2]/2)

        gv1 = geompy.MakeVertex(vol[0]/2, vol[1]/2, vol[2]/2)

        Gauge = geompy.MakeBoxTwoPnt(gv0, gv1)

        measured = geompy.MakeCommon( Gauge, self.Sample )




        # Restore rotations

        # Phi rotation
        
        measured = geompy.MakeRotation(measured, self.OZ, -self.initRot[2])


        
        # Omega rotation
        
        measured = geompy.MakeRotation(measured, enginx.OZ, -self.initRot[1])

        

        # Chi rotation
        
        measured = geompy.MakeRotation(measured, enginx.OY, -self.initRot[0])



        # Restore initial traslation

        measured = geompy.MakeTranslation(measured, -self.initTras[0], -self.initTras[1], -self.initTras[2])



        return measured

    

    


    def EulerRot(self, geompy, enginx, rot=(0,0,0)):

        
        """

        Euler-type rotations

        """


        degree = [x*np.pi/180.0 for x in rot]

        self.initRot = degree
        
        
        
        # Alpha rotation

        newSample = deepcopy(self)        
        
        newSample.Sample = geompy.MakeRotation(self.Sample, enginx.OZ, degree[0])

        newSample.OX = geompy.MakeRotation(self.OX, enginx.OZ, degree[0])

        newSample.OY = geompy.MakeRotation(self.OY, enginx.OZ, degree[0])

        newSample.OZ = geompy.MakeRotation(self.OZ, enginx.OZ, degree[0])        



        # Beta rotation
        
        newSample.Sample = geompy.MakeRotation(newSample.Sample, newSample.OX, degree[1])

        newSample.OY = geompy.MakeRotation(newSample.OY, newSample.OX, degree[1])

        newSample.OZ = geompy.MakeRotation(newSample.OZ, newSample.OX, degree[1])



        # Gamma rotation
        
        newSample.Sample = geompy.MakeRotation(newSample.Sample, newSample.OZ, degree[2])

        newSample.OX = geompy.MakeRotation(newSample.OX, newSample.OZ, degree[2])

        newSample.OY = geompy.MakeRotation(newSample.OY, newSample.OZ, degree[2])



        return newSample    
