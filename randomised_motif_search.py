"""
RandomisedMotifSearch:
Algorithm that picks a random k-mer from each string of dna that is input, calculates a profile from these.
Then enters a for loop that counts till 1000 (to have nice number of samples)
each loop, it generates a new set of motifs from the input dna strings and the matrix, 
calculates the score and if the motif
collection scores better, these motifs are now best_motifs.
if score is not better, loop is broken and best_motifs are returned.
Includes pseudocounts for less bias.
input: k, dna (string array)
output: best_motifs (k-mer array)
"""

import numpy as np
def random_motif_search(t,k,dna):
    best_motifs=random_kmer_generation(t,k,dna)
    
    for i in range (1000):
        prob_matrix = motif_matrix(best_motifs)
        motifs=[]
        for j in range (t):
            
            motifs.append(most_probable_kmer(dna[j],k,prob_matrix))
        if calculate_score(motifs) < calculate_score(best_motifs):
            best_motifs=motifs
        else:
            return best_motifs

def run_random_motif_search(t,k,dna, iterations=1000): 
    """
    Run the random_motif_search algorithm multiple times to find the best motifs.
    """
    best_motifs = None
    best_score = float('inf')

    for _ in range(iterations):
        motifs = random_motif_search(t,k,dna)
        current_score = calculate_score(motifs)

        if current_score < best_score:
            best_motifs = motifs
            best_score = current_score

    return best_motifs

def random_kmer_generation(t,k,dna):
    kmers=[]
    for i in range(t):
        random_int=np.random.randint(len(dna[0])-k+1)
        kmers.append(dna[i][random_int:random_int+k])
    return kmers
        

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
    return ((profile_matrix+1) /(t+4)) #implementation of pseudocounts so no base has a zero probability of occurring

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



#print(run_random_motif_search(5, 8,['CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA', 'GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG', 'TAGTACCGAGACCGAAAGAAGTATACAGGCGT', 'TAGATCAAGTTTCAGGTGCACGTCGGTGAACC', 'AATCCACCAGCTCCACGTGCAATGTTGGCCTA']))
f = open("dataset_30307_5 (1).txt", 'r').read().strip().splitlines('\n ')
#print(f[1])
strings = f[2].split(' ')
#print(strings)
print(run_random_motif_search(int(f[1].strip()),int(f[0].strip()),strings))
