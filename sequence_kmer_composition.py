"""
text composition problem
input string and int k, returns list of kmers found in the string, sorted in random order
"""

def text_comp(k,text):
    kmers=[]
    for i in range(len(text)-k+1):
        kmers.append(text[i:i+k])
    return " ".join(kmers)

f = open("dataset_30153_3 (1).txt", 'r').read().strip().splitlines('\n ')
text_comp(int(f[0]),f[1])
