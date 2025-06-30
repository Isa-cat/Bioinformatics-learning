"""
De Bruijn graph problem; solved from a string and input integer k 
(k=length of kmer)
returns:
adjacency list-representation of de Bruijn graph, with k-1-mers as glued nodes showing their adjacent edge
"""

from collections import defaultdict
def debruijn_adj_list(k,patterns):
    adjacency_dict=defaultdict(list)
    #k=len(patterns[0])
    #print(k)
    for kmer in patterns:
        #print(kmer)
        adjacency_dict[kmer[:-1]].append(kmer[1:])
    return adjacency_dict

#print(adjacency_list(['ATGCG', 'GCATG', 'CATGC', 'AGGCA', 'GGCAT', 'GGCAC']))
def write_to_doc(k,text):
    kmers=[text[i:i+k] for i in range(len(text)-k+1)]
    #print(kmers)
    edge_dict=debruijn_adj_list(k,kmers)
    with open("output.txt", "w") as file:
        for key, value in edge_dict.items():
            file.write(f"{key}: {' '.join(value)}\n")

f = open("dataset_30183_6.txt", 'r').read().strip().split('\n')
#print(f)
write_to_doc(int(f[0]),f[1])
