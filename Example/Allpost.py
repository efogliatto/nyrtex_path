import numpy as np

import matplotlib.pyplot as plt

import argparse

import os



if __name__ == "__main__":



    
    datos = np.loadtxt('Sample_fp_1.dat', unpack = True)
    
    for rot in range(0,5):

        plt.plot( datos[rot], label = rot )


    plt.legend( loc='best' )
        
    plt.show()



    
    
    for rot in range(5,11):

        plt.plot( datos[rot], label = rot )


    plt.legend( loc='best' )
        
    plt.show()    



    
    for rot in range(11,17):

        plt.plot( datos[rot], label = rot )


    plt.legend( loc='best' )
        
    plt.show()
