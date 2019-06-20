import numpy as np

import matplotlib.pyplot as plt

from matplotlib.ticker import MaxNLocator

import math

import argparse

import os



if __name__ == "__main__":



    # Carga de rotaciones con el formato especificado en el script de SALOME
    
    datos = np.loadtxt('M15_fp_0.dat', unpack = True)


    # Division de la lista por cantidad maxima de elementos

    nmax = 5

    my_list = [x for x in range(len(datos))]
  
    rotaciones = [my_list[i * nmax:(i + 1) * nmax] for i in range((len(my_list) + nmax - 1) // nmax )]



    # Figuras en subplot
    
    fig, axs = plt.subplots(math.ceil(len(rotaciones)/2), 2)

    j = 0

    for k in range(len(rotaciones)):

        i = math.floor(k/2)

        j = j % 2


        for rot in rotaciones[k]:

            axs[i][j].plot( range(1,len(datos[rot])+1), 1000*datos[rot], label = rot )


        

        axs[i][j].xaxis.set_major_locator(MaxNLocator(21,integer=True))

        axs[i][j].set_xlabel('Detector')

        axs[i][j].set_ylabel('Path [mm]')
            
        axs[i][j].legend( loc = 'best' )
            
        
        j = j+1


    plt.show()
