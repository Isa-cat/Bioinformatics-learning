import random
import numpy as np
from collections import Counter

def random_gen(probabilities):
    """
    Random number generator that will return an index based on weighted probabilites
    """
    prob_indices=[]
    c=float()
    for i in range (len(probabilities)):
        prob_indices.append(i)
        c+=probabilities[i]
    probabilities=probabilities/c
    return random.choices(prob_indices,k=1,weights=probabilities)[0]

def gibbs_sampler(k,t,N,dna):
    best_motifs=[]
    motifs=[]
    for seq in dna:
        index=random.randint(0,len(seq)-k)
        motifs.append(seq[index:index+k])
    best_motifs=motifs
    for j in range(N):
        i = random.randint(0,t-1)
        #print(i)
        if i < t:
            profile=motif_matrix(motifs[0:i]+motifs[i+1:])
        else:
            profile=motif_matrix(motifs[0:i])
        new_index=random_gen(motif_probabilities(profile,dna[i],k))
        motif_i=dna[i][new_index:(new_index+k)]
        motifs[i]=motif_i
        #print(motifs)
        #print(profile)
        if(calculate_score(motifs)<calculate_score(best_motifs)):
            best_motifs=motifs
        #print(best_motifs)
    return best_motifs

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
    return ((profile_matrix+1) /(t+4)) #implementation of pseudocounts so no base has a zero probability of occurring


def motif_probabilities(matrix, seq,k):
    """
    generates a kmer probability list from the string seq transferred to it, based on the 
    probability matrix it gets
    """
    prob_kmers=[]
    nucleotides = 'ATGC'
    for i in range(len(seq)-k):
        prob_kmer=1
        kmer=seq[i:i+k]
        
        for j in range(len(kmer)):
            #print(j)
            prob_kmer = prob_kmer * matrix[int(nucleotides.find(kmer[j]))][j]
        prob_kmers.append(prob_kmer)
    return prob_kmers

def calculate_score(patterns):
    """
    calculates the score (=distance from consensus string) of the array of patterns it gets, returns score
    """
    #prob_matrix=motif_matrix(patterns)
    #bases = 'ATGC'
    #consensus_string=str()
    score=0
    for i in range(len(patterns[0])):
        col = [motif[i] for motif in patterns]
        most_common = Counter(col).most_common(1)[0][1]
        score += len(patterns) - most_common
    #for i in range(len(patterns[0])):
        #consensus_string+=str(bases[prob_matrix[:,i].argmax()])
    #for j in range(len(patterns)):
        #for f in range(len(patterns[0])):
            #if patterns[j][f] == consensus_string[f]:
                #pass
            #else:
                #score+=1
    return score

def run_gibbs_sampler(k,t,N,dna,iterations=40):
    """
    Run the RandomizedMotifSearch algorithm multiple times to find the best motifs.
    """
    best_motifs = []
    best_score = float('inf')

    for _ in range(iterations):
        motifs = gibbs_sampler(k,t,N,dna)
        current_score = calculate_score(motifs)

        if float(current_score) < float(best_score):
            best_motifs = motifs
            best_score = current_score
    return " ".join(best_motifs)


#print(run_gibbs_sampler(8,5,100,['CGCCCCTCTCGGGGGTGTTCAGTAACCGGCCA', 'GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG', 'TAGTACCGAGACCGAAAGAAGTATACAGGCGT', 'TAGATCAAGTTTCAGGTGCACGTCGGTGAACC', 'AATCCACCAGCTCCACGTGCAATGTTGGCCTA']))

f = open("dataset_30309_11 (4).txt", 'r').read().strip().splitlines('\n ')
nums=f[0].split(' ')
strings = f[1].split(' ')
#print(strings)
print(run_gibbs_sampler(int(nums[0]),int(nums[1]),int(nums[2]), strings))
