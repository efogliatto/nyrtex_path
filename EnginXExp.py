import salome

import numpy as np



class EnginXExp:

    """

    Engin-X Experiment class
    

    """

    def __init__(self, geompy, Nx=2, Nz=5, pub_det=True, pub_lines=True, detFile='none'):

        
        """
        Default constructor

        North and south bank with equal grid
        """


        # Create origin and add to study

        self.O = geompy.MakeVertex(0, 0, 0)
        
        self.OX = geompy.MakeVectorDXDYDZ(1, 0, 0)

        self.OY = geompy.MakeVectorDXDYDZ(0, 1, 0)

        self.OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)

        geompy.addToStudy( self.O, 'O' )

        geompy.addToStudy( self.OX, 'OX' )

        geompy.addToStudy( self.OY, 'OY' )

        geompy.addToStudy( self.OZ, 'OZ' )
        
        

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

        for j in reversed( range(Nz) ):

            for i in range(Nx):            

                dx = 0.4 / Nx

                dz = 0.8 / Nz

                self.nb_detectors.append(  geompy.MakeVertex(-0.2 + dx * (0.5 + i),  1.5, -0.4 + dz * (0.5 + j) )  )

                self.sb_detectors.append(  geompy.MakeVertex( 0.2 - dx * (0.5 + i), -1.5, -0.4 + dz * (0.5 + j) )  )                



        # Write detector coordinates if name is provided

        if detFile != 'none':

            with open( detFile, 'w' ) as dfile:


                # North bank

                dfile.write('# North bank\n')

                for vtx in self.nb_detectors:

                    coord = geompy.PointCoordinates(vtx)

                    dfile.write('{:.5f} {:.5f} {:.5f}\n'.format( coord[0],coord[1],coord[2] ))




                # South bank

                dfile.write('\n# South bank\n')

                for vtx in self.sb_detectors:

                    coord = geompy.PointCoordinates(vtx)

                    dfile.write('{:.5f} {:.5f} {:.5f}\n'.format( coord[0],coord[1],coord[2]) )
                    
                    
                

        # Add detectors to study

        if pub_det:

            for i,dt in enumerate( self.nb_detectors ):

                geompy.addToStudy( dt, 'NB-Detector {}'.format(i+1) )


            for i,dt in enumerate( self.sb_detectors ):

                geompy.addToStudy( dt, 'SB-Detector {}'.format(i+1) )            





        # Neutron lines

        self.nb_lines = []

        self.sb_lines = []

        
        for det in self.nb_detectors:

            self.nb_lines.append( geompy.MakeLineTwoPnt(self.O, det) )


        for det in self.sb_detectors:

            self.sb_lines.append( geompy.MakeLineTwoPnt(self.O, det) )


        if pub_lines:

            for i,nl in enumerate( self.nb_lines ):
                
                geompy.addToStudy( nl, 'NB-Line {}'.format(i+1) )

            for i,nl in enumerate( self.sb_lines ):
                
                geompy.addToStudy( nl, 'SB-Line {}'.format(i+1) )                
            






        # Beam
        
        Vertex_beam = geompy.MakeVertex(-3, 0, 0)
        
        self.BEAM = geompy.MakeLineTwoPnt(Vertex_beam, self.O)

        geompy.addToStudy(self.BEAM, "Beam")
        
                
        pass




    

    # Flight paths

    def paths(self, geompy, sample, show=False, name='sample'):

        """

        Compute paths for specific sample
        
        """

        nb_paths = [ geompy.MakeCommon(self.BEAM, sample) ]

        sb_paths = [ geompy.MakeCommon(self.BEAM, sample) ]

        
        for nl in self.nb_lines:

            nb_paths.append(  geompy.MakeCommon(nl, sample)  )

            
        for nl in self.sb_lines:

            sb_paths.append(  geompy.MakeCommon(nl, sample)  )



        if show:

            for nl in nb_paths:

                geompy.addToStudy(nl,name + '_NB')

            for nl in sb_paths:

                geompy.addToStudy(nl,name + '_SB')                


        return nb_paths, sb_paths



    

    # Flight distances

    def flight_distance(self, geompy, sample, show=False, name='sample'):

        """

        Compute distances for specific sample
        
        """

        nb_path, sb_path = self.paths(geompy,sample, show, name)


        nb_dist = []

        sb_dist = []


        for fp in nb_path:

            nb_dist.append( geompy.BasicProperties(fp)[0] )


        for fp in sb_path:

            sb_dist.append( geompy.BasicProperties(fp)[0] )       

        

        return nb_dist[1:] + sb_dist[1:], nb_dist[0]
