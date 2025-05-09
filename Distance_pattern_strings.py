"""
Function to calculate the distance between a pattern and an array of strings, where the closest version of the pattern has to be found (and 
distance calculated from it to pettern)
input: string pattern, array of strings dna
output: d(pattern, dna)
"""

import numpy as np

def Distance_Patterns_Strings(pattern, dna):
    k=len(pattern)
    distance=0
    for seq in dna:
        hamm_dist=k+1
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
        

f = open("dataset_30312_1.txt", 'r').read().splitlines()
pattern = f[0]
dna = f[1].split(" ")
Distance_Patterns_Strings(pattern, dna)
