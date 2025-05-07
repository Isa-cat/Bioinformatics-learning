"""
Computing Shannon Entropy:
Input: Array of Strings
output: Shannon Entropy
creates matrix of strings with size t x k (t=number of strings, k = length of strings)
"""
import pandas as pd
import numpy as np
def Motif_Matrix(pattern_array):
    t = len(pattern_array)
    k=len(pattern_array[0])
    profile_matrix=pd.DataFrame(index=['A','T','G','C'], columns =range(k))
    for j in range(k):
        count_dict={'A':0,'T':0,'G':0,'C':0}
        for i in range(t):
            count_dict[pattern_array[i][j]]+=1
        for key in count_dict:
            profile_matrix.loc[key,k]=count_dict[key]/t
    print(profile_matrix)
    return profile_matrix

def Shannon_Entropy(pattern_array):
    entropy=0
    freq_matrix=Motif_Matrix(pattern_array)
    for i in range (freq_matrix.shape[0]):
        for j in range(freq_matrix.shape[1]):
            if freq_matrix.iloc[i][j] >0:
                entropy= entropy-(freq_matrix.iloc[i][j]*np.log2(freq_matrix.iloc[i][j]))
            else: pass
    return entropy

motifs= ['TCGGGGGTTTTT', 'CCGGTGACTTAC', 'ACGGGGATTTTC', 'TTGGGGACTTTT', 'AAGGGGACTTCC', 'TTGGGGACTTCC', 'TCGGGGATTCAT', 'TCGGGGATTCCT', 'TAGGGGAACTAC', 'TCGGGTATAACC']
print(Shannon_Entropy(motifs))
