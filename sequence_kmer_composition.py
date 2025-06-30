"""
text composition problem
input string and int k, returns list of kmers found in the string, sorted in random order
"""

def text_comp(k,text):
    kmers=[]
    for i in range(len(text)-k+1):
        kmers.append(text[i:i+k])
    return " ".join(kmers)

f = open("dataset_30153_3 (1).txt", 'r').read().strip().splitlines('\n ')
text_comp(int(f[0]),f[1])


"""
String reconstruction problem, easy version: kmers are given as input in the order so that the last k-1 bases of kmer(i) equal the k-1 first bases of kmer(i+1)
input: collection of kmers
output: reconstructed string
"""

def kmers_to_string(kmers):
    string=kmers[0]
    for pattern in kmers[1:]:
        string+=pattern[-1]
    return string

print(kmers_to_string(f[0].split(' '))) 
#print(f[0].split(' '))
f = open("dataset_30182_3.txt", 'r').read().strip().splitlines('\n ')


"""
Overlap Graph: string adjacency problem
input: collection of patterns
output: adjacency list as a txt file
"""
from collections import defaultdict
def adjacency_list(patterns):
    adjacency_dict=defaultdict(list)
    k=len(patterns[0])
    for kmer in patterns:
        for kmer2 in patterns:
            if kmer!=kmer2:
                if kmer[1:] == kmer2[0:k-1]:
                    adjacency_dict[kmer].append(kmer2)
            else:
                pass
    return adjacency_dict

#print(adjacency_list(['ATGCG', 'GCATG', 'CATGC', 'AGGCA', 'GGCAT', 'GGCAC']))
def write_to_doc(patterns):
    edge_dict=adjacency_list(patterns)
    with open("output.txt", "w") as file:
        for key, value in edge_dict.items():
            file.write(f"{key}: {' '.join(value)}\n")



#write_to_doc(['ATGCG', 'GCATG', 'CATGC', 'AGGCA', 'GGCAT', 'GGCAC'])
write_to_doc(f[0].split(' '))
#print(f[0].split(' '))
f = open("dataset_30182_10 (1).txt", 'r').read().strip().splitlines('\n ')
