import pandas as pd
import networkx as nx
import numpy as np
import itertools
import networkx.algorithms.isomorphism as iso
from tqdm import tqdm

"""
This program is intended to remove self-loops from an adjacency list
"""

adjlist = np.loadtxt('/Users/pablorosillo/Library/CloudStorage/OneDrive-UniversitatdelesIllesBalears/Máster IFISC/Asignaturas/Systems Biology/Final project/mfinder1.2/network.txt')

adjlistaux = np.ones((np.shape(adjlist)[0],3)); 
adjlistaux[:,0] = adjlist[:,0];
adjlistaux[:,1] = adjlist[:,1];
adjlist = adjlistaux;

trm = [];

for i in range(np.shape(adjlist)[0]):
    adjlist[i][2] = 1;
    if adjlist[i][0] == adjlist[i][1]:
        trm.append(i);
        
adjlist2 = np.delete(adjlist, trm, 0);


np.savetxt(r'/Users/pablorosillo/Library/CloudStorage/OneDrive-UniversitatdelesIllesBalears/Máster IFISC/Asignaturas/Systems Biology/Final project/mfinder1.2/network.txt', adjlist2, fmt='%.0f', delimiter=' ', newline='\n', header='', footer='', comments='# ', encoding=None)

