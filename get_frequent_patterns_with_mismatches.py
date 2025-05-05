"""
Frequent words problem, allowing up to d mismatches: goes over text, for each pattern makes a set of neighbors (patterns with d mismatches)
each of the patterns is added to the freqmap dict if not yet in, gets one added to them.
maximum value in the dictionary is found, returns the patterns occuring at that value.
"""


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
        if Hamming_Distance(neighbor, pattern[1:]) <= d:
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
    Find maximal onumber of occurence and which pattern achieves that
    return those patterns
    """
    frequent_words = []
    freq_map={}
    for i in range (len(text)-k+1):
        neighbor_patterns=Generate_Neighbors(text[i:i+k],d)
        for key in neighbor_patterns:
            #print(key)
            if key in freq_map.keys():
                freq_map[key]= freq_map[key]+1
            else:
                freq_map[key]=1
    max_freq = max(freq_map.values())
    #print(max_freq)
    for key in freq_map:
        if freq_map[key] == max_freq:
            #print(key)
            frequent_words.append(key)
    return frequent_words


def MaxMap(freq_map):
    return max(freq_map.values())
genome_file=open('dataset_30278_6 (1).txt','r')
filedata=genome_file.readlines()
genome_file.close()
MismatchedFrequentWords(filedata[1].strip(), filedata[0].strip(),int(filedata[2].strip())) #strip() to remove any whitespace characters   

