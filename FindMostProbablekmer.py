"""
Function to calculate the most probable k-mer in a string text, as calculated with a profile matrix. 
input: int k, string text, matrix (4xk size)
output: string k-mer

"""

def Most_Probable_kmer(text, k, profile):
    nucleotides='ACGT'
    pattern=str()
    probability=float(0)
    for i in range (len(text)-k+1):
        kmer=text[i:i+k]
        prob_kmer=1
        for j in range(len(kmer)):
            
            prob_kmer=prob_kmer*profile[int(nucleotides.find(kmer[j]))][j]
        if prob_kmer > probability:
            pattern=kmer
            probability=prob_kmer
    return pattern
def Read_Data_From_File(file):
    matrix = []
    for line in file:
        fields = [float(num) for num in line.strip().split(' ')] #arrays first read in as a string, so each number needs to be converted into a float before it works
        matrix.append(fields)
    return matrix
    
#Most_Probable_kmer('ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT',5,[[0.2, 0.2, 0.3, 0.2, 0.3],[0.4, 0.3, 0.1, 0.5, 0.1],[0.3, 0.3, 0.5, 0.2, 0.4],[0.1, 0.2, 0.1, 0.1, 0.2]])

f = open("dataset_30305_3.txt", 'r').read().splitlines()
#print(f[0])

freqs = f[2:]
profile_matrix = Read_Data_From_File(freqs)
#print(profile_matrix)
Most_Probable_kmer(f[0],int(f[1]),profile_matrix)
