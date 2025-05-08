"""
Computing Shannon Entropy:
Input: Array of Strings
output: Shannon Entropy
creates matrix of strings with size t x k (t=number of strings, k = length of strings)
"""
import numpy as np
def Motif_Matrix(pattern_array):
    t = len(pattern_array)
    k=len(pattern_array[0])
    profile_matrix=np.zeros((4,k))
    bases='ATGC'
    for seq in pattern_array:
        #count_dict={'A':0,'T':0,'G':0,'C':0}
        for i in range(k):
            base=bases.find(seq[i])
            profile_matrix[base,i]+=1
        
    print(profile_matrix/t)
    return profile_matrix/t

def Shannon_Entropy(pattern_array):
    entropy=0
    freq_matrix=Motif_Matrix(pattern_array)
    for i in range (freq_matrix.shape[0]):
        for j in range(freq_matrix.shape[1]):
            if freq_matrix[i][j] >0:
                entropy= entropy-(freq_matrix[i][j]*np.log2(freq_matrix[i][j]))
            else: pass
    return entropy

motifs= ['TCGGGGGTTTTT', 'CCGGTGACTTAC', 'ACGGGGATTTTC', 'TTGGGGACTTTT', 'AAGGGGACTTCC', 'TTGGGGACTTCC', 'TCGGGGATTCAT', 'TCGGGGATTCCT', 'TAGGGGAACTAC', 'TCGGGTATAACC']
print(Shannon_Entropy(motifs))
