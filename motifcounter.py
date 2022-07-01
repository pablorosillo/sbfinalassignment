import networkx as nx
import numpy as np
import itertools
import networkx.algorithms.isomorphism as iso
from tqdm import tqdm


def mcounter(gr, mo, comp):
    
    """
    Counts motifs in a directed graph
    gr: A DiGraph object
    mo: dict of motifs to count
    comp: flag for comparing also weights
    returns: A dict with the number of each motifs, with the same keys as mo
    
    """
    #This function will take each possible subgraphs of gr of SIZE 3 (or any other if we want 
    # to modify it), then compare them to the mo dict using .subgraph() and is_isomorphic

    mcount = dict(zip(mo.keys(), list(map(int, np.zeros(len(mo))))))
    nodes = gr.nodes()

    #We use iterools.product to have all combinations of three nodes in the
    #original graph. 

    triplets = list(itertools.product(*[nodes, nodes, nodes]))
    triplets = [trip for trip in tqdm(triplets) if len(list(set(trip))) == 3]
    triplets = map(list, map(np.sort, triplets))
    u_triplets = []
    [u_triplets.append(trip) for trip in triplets if not u_triplets.count(trip)]

    
    em = iso.numerical_edge_match("weight", 1)

        
    if comp == 1:
        
        for trip in tqdm(u_triplets):
            sub_gr = gr.subgraph(trip)
    
            mot_match = list(map(lambda mot_id: nx.is_isomorphic(sub_gr, mo[mot_id], edge_match=em), motifs.keys()))
            match_keys = [list(mo.keys())[i] for i in range(len(mo)) if mot_match[i]]
            if len(match_keys) == 1:
                mcount[match_keys[0]] += 1
        
    else:
        
        for trip in tqdm(u_triplets):
            sub_gr = gr.subgraph(trip)
        
            mot_match = list(map(lambda mot_id: nx.is_isomorphic(sub_gr, mo[mot_id]), motifs.keys()))
            match_keys = [list(mo.keys())[i] for i in range(len(mo)) if mot_match[i]]
            if len(match_keys) == 1:
                mcount[match_keys[0]] += 1
            

    return mcount


adjlist1 = [(1,2,1), (2,3,1), (1,3,1)];

motifs = {
    'S1': nx.DiGraph((x, y, {'weight': v}) for (x, y, v) in adjlist1),
    }

adjlistecoli = np.loadtxt('/Users/pablorosillo/Library/CloudStorage/OneDrive-UniversitatdelesIllesBalears/Máster IFISC/Asignaturas/Systems Biology/Final project/mfinder1.2/network_exmp.txt')

G = nx.DiGraph((x, y, {'weight': v}) for (x, y, v) in adjlistecoli)
print(*G.edges(data=True), sep='\n')

print(mcounter(G, motifs, 0))



