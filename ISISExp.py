import salome

import numpy as np



class ISISExp:

    """

    ISIS Experiment class
    

    """

    def __init__(self, geompy, Nx=1, Ny=1):
        
        """
        Default constructor

        North and south bank with equal grid
        """


        # North bank
        Vertex_1 = geompy.MakeVertex(1.5, -0.2, -0.4)
        Vertex_2 = geompy.MakeVertex(1.6, 0.2, 0.4)
        self.north_bank = geompy.MakeBoxTwoPnt(Vertex_1, Vertex_2)

        #South bank
        Vertex_3 = geompy.MakeVertex(-1.5, -0.2, -0.4)
        Vertex_4 = geompy.MakeVertex(-1.6, 0.2, 0.4)
        self.south_bank = geompy.MakeBoxTwoPnt(Vertex_3, Vertex_4)
        
        pass
