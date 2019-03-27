import salome

import numpy as np



class EnginXExp:

    """

    Engin-X Experiment class
    

    """

    def __init__(self, geompy, Nx=2, Nz=5):

        
        """
        Default constructor

        North and south bank with equal grid
        """


        # North bank
        
        Vertex_1 = geompy.MakeVertex(-0.2, 1.5, -0.4)

        Vertex_2 = geompy.MakeVertex(0.2, 1.6, 0.4)

        self.north_bank = geompy.MakeBoxTwoPnt(Vertex_1, Vertex_2)

        geompy.addToStudy( self.north_bank, 'North Bank' )
        

        
        # South bank

        Vertex_3 = geompy.MakeVertex(-0.2, -1.6, -0.4)

        Vertex_4 = geompy.MakeVertex(0.2, -1.5, 0.4)

        self.south_bank = geompy.MakeBoxTwoPnt(Vertex_3, Vertex_4)
               
        geompy.addToStudy( self.south_bank, 'South Bank' )


        
        # Detectors

        self.nb_detectors = []

        self.sb_detectors = []        

        for j in range(Nz):

            for i in range(Nx):            

                dx = 0.4 / Nx

                dz = 0.8 / Nz

                self.nb_detectors.append(  geompy.MakeVertex(-0.2 + dx * (0.5 + i),  1.5, -0.4 + dz * (0.5 + j) )  )

                self.sb_detectors.append(  geompy.MakeVertex(-0.2 + dx * (0.5 + i), -1.5, -0.4 + dz * (0.5 + j) )  )                



        # Add detectors to study

        for i,dt in enumerate( self.nb_detectors ):

            geompy.addToStudy( dt, 'NB-Detector {}'.format(i) )


        for i,dt in enumerate( self.sb_detectors ):

            geompy.addToStudy( dt, 'SB-Detector {}'.format(i) )            
        
        
        pass
