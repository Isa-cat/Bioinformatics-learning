"""
Mismatched pattern search for most frequent patterns occuring also in their reverse complement
takes: input sequence, k (length of patter), d (max Hamming distance)
output: patterns (or mismatched patterns) that occur most often, in both forward and reverse reading 

"""
from collections import defaultdict
def Generate_Neighbors(pattern, d):
    patterns=set()
    nucleotides=['A','G','C','T']
    if d == 0: #if no deviation allowed, no neighbors, only pattern
        return pattern
    #elif d == 1:
        #return {'A','C','G','T'}
    elif len(pattern)==0:
        return {''}
    suffix_neighbors=Generate_Neighbors(pattern[1:],int(d))
           
    for neighbor in suffix_neighbors:
        if Hamming_Distance(neighbor, pattern[1:]) < d:
            for nuc in nucleotides:
                patterns.add(nuc+neighbor)
        else:
            patterns.add(pattern[0]+neighbor)
    return patterns

    
def Hamming_Distance(seq1,seq2):
    hamming_dist=0
    if len(seq1) == len(seq2):
        for i in range (len(seq1)):
            if seq1[i] == seq2[i]:
                pass
            elif seq1[i] != seq2[i]:
                hamming_dist+=1
    else:
        return('Please provide two sequence of same length.')
    return int(hamming_dist)

def MismatchedFrequentWords(text, k, d):
    """
    initiate empty array for frequent patterns and dictionary for frequency collection; generate pattern neighbors and then add their frequencies.
    Find maximal number of occurence and which pattern achieves that
    return those patterns
    """
    frequent_words = []
    freq_map=defaultdict(int)
    for i in range (len(text)-k+1):
        neighbor_patterns=Generate_Neighbors(text[i:i+k],d)
        for key in neighbor_patterns:
            #print(key)
            freq_map[key]+= 1
            freq_map[CreateComplementSequence(key)]+= 1
    max_freq = max(freq_map.values())
    #print(max_freq)
    for key in freq_map:
        if freq_map[key] == max_freq:
            #print(key)
            frequent_words.append(key)
    return frequent_words

def CreateComplementSequence(sequence):
    sequence=sequence.upper()
    clean_seq=str().join(filter(str.isalpha, sequence))
    #print(clean_seq)
    complement=str()
    for i in range (len(clean_seq)):
         #print(clean_seq[i])
         if clean_seq[i] == 'A':
             complement=complement+('T')
         if clean_seq[i] == 'C':
             complement=complement+('G')
         if clean_seq[i] == 'G':
             complement=complement+('C')
         if clean_seq[i] == 'T':
             complement=complement+('A')
         else:
             pass
    #print(complement)
    return ReverseSequence(complement)

def ReverseSequence(seq):
    reverse=seq[::-1]
#slices with negative steps and so starts at the back and moves to start of original string
    return reverse
def MaxMap(freq_map):
    return max(freq_map.values())


genome_file=open('dataset_30278_10.txt','r')
filedata=genome_file.readlines()
genome_file.close()
MismatchedFrequentWords(filedata[0].strip(), 5,3) #strip() to remove any whitespace characters
