import pandas as pd
import networkx as nx
import numpy as np
import itertools
import networkx.algorithms.isomorphism as iso
from tqdm import tqdm

"""
This program is intended to remove repeated connections between edges which may happen in non-
directed networks or in raw data (The Blacklist, for example)
"""

adjlist = np.loadtxt('/Users/pablorosillo/Library/CloudStorage/OneDrive-UniversitatdelesIllesBalears/Máster IFISC/Asignaturas/Systems Biology/Final project/mfinder1.2/network.txt')

trm = [];

for i in tqdm(range(np.shape(adjlist)[0])):
    for j in range(i+1,np.shape(adjlist)[0]):
        if adjlist[i][0] == adjlist[j][1] and adjlist[i][1] == adjlist[j][0]:
            trm.append(j);
        
adjlist2 = np.delete(adjlist, trm, 0);


np.savetxt(r'/Users/pablorosillo/Library/CloudStorage/OneDrive-UniversitatdelesIllesBalears/Máster IFISC/Asignaturas/Systems Biology/Final project/mfinder1.2/network.txt', adjlist2, fmt='%.0f', delimiter=' ', newline='\n', header='', footer='', comments='# ', encoding=None)

