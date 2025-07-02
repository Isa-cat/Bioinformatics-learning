"""
reconstructing a debruijn graph from a set of kmers
input: string patterns

each kmer is assigned to unconnected edge
the edge has two nodes: prefix, suffix

the unconnected edges are then used to make debruin graph with glued nodes, output as adjacency list
"""
from collections import defaultdict
def debruijn_adj_list(patterns):
    adjacency_dict=defaultdict(list)
    #k=len(patterns[0])
    #print(k)
    for kmer in patterns:
        #print(kmer)
        adjacency_dict[kmer[:-1]].append(kmer[1:])
    return adjacency_dict




def write_to_doc(kmers):
    edge_dict=debruijn_adj_list(kmers)
    with open("output.txt", "w") as file:
        for key, value in edge_dict.items():
            file.write(f"{key}: {' '.join(value)}\n")

#write_to_doc((['GAGG', 'CAGG', 'GGGG', 'GGGA', 'CAGG', 'AGGG', 'GGAG']))
f = open("dataset_30184_8.txt", 'r').read().strip().split('\n')
#print(f)
write_to_doc(f[0].split(' '))
