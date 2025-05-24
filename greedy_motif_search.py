"""
Function to perform greedy profile search:
takes dna collection of strings, k length of pattern and
makes first a profile matrix out of the 1st pattern in
1st string. then finds pattern in 2nd string most closely matching, recalculates
profile matrix (and so on).
When finished running over all strings, calculates Score of the
collection of motifs, if better than before: set as BestScoringMotifs
then sets reading frame one further on string0

output: string array bestmotifs

"""
import numpy as np
def greedy_motif_search(dna,k):
    t=len(dna)
    best_motifs=[seq[0:k+1] for seq in dna]
    for i in range (len(dna[0])-k+1):
        pattern=dna[0][i:i+k]
        motif_collection=[pattern]
        for j in range (1,t):
            prob_matrix = motif_matrix(motif_collection)
            motif_collection.append(most_probable_kmer(dna[j],k,prob_matrix))
        if calculate_score(motif_collection) < calculate_score(best_motifs):
            best_motifs=motif_collection
    return best_motifs

def calculate_score(patterns):
    prob_matrix=motif_matrix(patterns)
    bases = 'ATGC'
    consensus_string=str()
    score=0
    for i in range(len(patterns[0])):
        consensus_string+=str(bases[prob_matrix[:,i].argmax()])
    for j in range(len(patterns)):
        for f in range(len(patterns[0])):
            if patterns[j][f] == consensus_string[f]:
                pass
            else:
                score+=1
    return score



def motif_matrix(pattern_array):
    t = len(pattern_array)
    k = len(pattern_array[0])
    profile_matrix = np.zeros((4, k))
    bases = 'ATGC'
    for seq in pattern_array:
        for i in range(k):
            base = bases.find(seq[i])
            profile_matrix[base, i] += 1

    #print(profile_matrix / t)
    return profile_matrix / t

def most_probable_kmer(text, k, profile):
    nucleotides = 'ATGC'
    pattern = text[0:k]
    probability = float(0)
    for i in range(len(text) - k + 1):
        kmer = text[i:i + k]
        prob_kmer = 1
        for j in range(len(kmer)):
            prob_kmer = prob_kmer * profile[int(nucleotides.find(kmer[j]))][j]
        if prob_kmer > probability:
            pattern = kmer
            probability = prob_kmer
    return pattern



#print(greedy_motif_search(['GGCGTTCAGGCA', 'AAGAATCAGTCA', 'CAAGGAGTTCGC', 'CACGTCAATCAC', 'CAATAATATTCG'],3))
f = open("dataset_30305_5.txt", 'r').read().splitlines('\n ')
print(f[1])


print(greedy_motif_search(f[1].split(' '), int(f[0])))
