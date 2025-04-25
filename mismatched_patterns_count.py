#Frequent Word Mismatched Count: takes a pattern, allows d mismatches, counts all occurences of pattern (+- d mismatches) in a given text
def MismatchPatternCount(text, pattern,d):
    print(d)
    print(pattern)
    print(text)
    count=0
    for i in range (len(text)-len(pattern)+1):
        if Hamming_Distance(text[i:i+len(pattern)], pattern) <= d:
            count=count+1
    return count
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
#print(MismatchPatternCount('TTTAGAGCCTTCAGAGG', 'GAGG', 2))

genome_file=open('dataset_30278_6 (1).txt','r')
filedata=genome_file.readlines()
genome_file.close()
MismatchPatternCount(filedata[1].strip(), filedata[0].strip(),int(filedata[2].strip())) #strip() to remove any whitespace characters
