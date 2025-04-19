import numpy as np

"""
To find base k-mers that occur several times in a part of a genomic sequence: 
A sequence and k (length of k-mer), length L of the sequence window to be checked 
(where the pattern should be clustered), and minimum number of times the pattern should occur in the cluster (t)
is given to the FindCluster function, which creates an 
empty list for later. It also calls the FrequencyTable function to create a dictionary of the 
frequency of each base sequence of length k in the sequence window. MaxMap will then find the 
highest frequency as saved in the dictionary, and the list of k-mers is compared against the highest 
frequency value: all k-mers that occur at that frequency are added to
the list of frequent words and finally, printed.
"""
def FindCluster(seq, k, L, t):
    patterns=[]
    n =len(seq)
    #pattern_list=str()

    freq_map = FrequencyTable(seq[0:L+1], k) #first frame to go over
    for key in freq_map.keys():
        if freq_map[key] >= t:
            if key in patterns:
                pass
            else:
                patterns.append(key) #see if any k-mers appear more often than threshold value t
    for i in range(1,n-L+1):        #to simplify search, remove one count from frequency table of the first k-mer
        #seq_window = seq[i:L + i]
        key = seq[i+L-k:i+L]
        freq_map[seq[i-1:i-1+k]]=freq_map[seq[i-1:i-1+k]]-1
        if key in freq_map.keys(): #append one count of the new k-mer that is found
            freq_map[key]+=1
        else:
            freq_map[key] =1
        if freq_map[key] >= t:
                if key in patterns:
                    pass
                else:
                    patterns.append(key) #check if k-mer is above t threshold
    return patterns

def FrequencyTable(text,k):
    freq_dict={}
    for i in range (len(text)-k+1):
        key=str(text[i:i+k])
        if key in freq_dict.keys():
            freq_dict[key]= freq_dict[key]+1
        else:
            freq_dict[key]=1
        #print(text[i:i+k])
    #print(freq_dict)
    return freq_dict

genome_file=open('E_coli.txt','r')
genome=genome_file.readline()
genome_file.close()
print(FindCluster(genome,9 ,500, 3))