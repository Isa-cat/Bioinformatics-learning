"""
Creation of MedianString: the pattern that has the lowest d(medianstring,dna)
input: k (length of pattern) and dna (array of strings)
"""

import numpy as np

"""
Brute force MedianString: generates ALL possible patterns, and checks if the distance to dna is lower than before
"""

def Median_String(k, dna):
    distance=float('inf')
    kmers=Generate_kmers(k)
    for kmer in kmers:



def Generate_kmers(k):
    nucleotides='ATCG'
    kmers=('A','T','C','G')
    for i in range(k):
        for kmer in kmers:
            for j in range(4):
                
