"""
Creation of MedianString: the pattern that has the lowest d(medianstring,dna)
input: k (length of pattern) and dna (array of strings)
"""

import numpy as np
import itertools
"""
Brute force MedianString: generates ALL possible patterns, and checks if the distance to dna is lower than before
combinations creates all possible combinations of given set of characters, with arguments characters, length (of combined object)
"""

def Median_String(k, dna):
    distance=float('inf')
    median=str()
    kmers=Generate_kmers(k)
    for kmer in kmers:
        if distance > Distance_Patterns_Strings(kmer,dna):
            distance = Distance_Patterns_Strings(kmer,dna)
            median=kmer
    return median


def Generate_kmers(k):
    #print([''.join(combination) for combination in itertools.product('ATCG',repeat=int(k))]) #for test purposes
    return ([''.join(combination) for combination in itertools.product('ATCG',repeat=int(k))]) #makes an array for every combination created by product() instead of a comma-separated tuple

def Distance_Patterns_Strings(pattern, dna):
    k=len(pattern)
    distance=0
    for seq in dna:
        hamm_dist=float('inf')
        for i in range(len(seq)-k+1):
            if Hamming_Distance(seq[i:i+k],pattern) < hamm_dist:
                hamm_dist= Hamming_Distance(seq[i:i+k],pattern)
        distance=distance+hamm_dist
    return distance

def Hamming_Distance(seq1,seq2):
    hamming_dist=0
    if len(seq1) == len(seq2):
        for i in range (len(seq1)):
            if seq1[i] == seq2[i]:
                pass
            elif seq1[i] != seq2[i]:
                hamming_dist+=1
    else:
        return('Please provide two sequences of same length.')
    return int(hamming_dist)

#Median_String(3, ['AAATTGACGCAT', 'GACGACCACGTT', 'CGTCAGCGCCTG', 'GCTGAGCACCGG', 'AGTTCGGGACAG'])
           
f = open("dataset_30304_9.txt", 'r').read().splitlines()
#print(f[0])
#for testing purposes
dna = f[1:]
#print(dna) 
# for testing purposes
Median_String(int(f[0]), dna)   
