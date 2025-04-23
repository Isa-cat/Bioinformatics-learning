def ApproximatePatternCount(pattern, text, dev):
    count=0
    length=len(pattern)
    indices=str()
    for i in range (len(text)-length+1): 
        hamming_dist=Hamming_Distance(text[i:i+length], pattern)
        if (hamming_dist<=dev) or (text[i:i+length] == pattern): 
            indices = indices+str(i)+' '
        else:
            pass
    return indices
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
    return hamming_dist

genome_file=open('dataset_30278_4.txt','r')
filedata=genome_file.readlines()
genome_file.close()
ApproximatePatternCount(filedata[0], filedata[1],int(filedata[2]))
#ApproximatePatternCount('ATTCTGGA', 'CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT',3)
