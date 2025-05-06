"""
Brute-force approach to searching a collection of DNA strings for k-mer patterns 
(with d mismatches allowed) that occur in all strings in the array
d,k: int; d: mismatch number, k: length of pattern
dna: array of strings
output: set of strings
"""

def Motif_Enumeration(dna, k, d):
    patterns=set()
    all_motifs=set()
    for string in dna:
        for i in range(len(string)-k+1):
            neighbors=Generate_Neighbors(string[i:i+k],d)
            all_motifs.update(neighbors)    #add all neighbors with d to set of all patterns set
    for pattern in all_motifs: #iterate over list of all patterns
        match=True #variable match set to True, to later on break loop (or not)
        for seqstring in dna: #iterate over the strings in dna
            found=False #variable found set to False, to break loop (or not)
            for i in range(len(seqstring)-k+1):
                if Hamming_Distance(pattern, seqstring[i:i+k])<=d:
                    found=True #if the pattern matches the substring with max d mismatches, pattern was found, iteration proceeds to next string in dna
                    break
            if not found: #if at end of loop over string pattern not found, match set to False, iteration broken
                match=False
                break
        if match==True: #only patterns that were found in all seqstrings (match still True) get added to patterns
            patterns.add(pattern)
    return patterns
        
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

Motif_Enumeration(['TCCACATATGATATCATACTGGCTG','TCCACGGGGCGGTTCATGTTCCTCG', 'GAGAGCAACTCTCTGTCCACTCGAC', 'TCCCTTATAACTTTGCGCCTGGTCG', 'TGTCATCCGGTTCACGAGGGGACTA' ,'TACGACTATTCATCTCAGGTTCCCC'], 5,2)
