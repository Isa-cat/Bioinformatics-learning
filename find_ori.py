import numpy as np
def FindOri(genome):
    """
    the function needs to calculate the skew across
    a whole genome, determine the lowest skew value that can be calculated and return the 
    index of the position with that value.
    It should first call the Skew calculator function, and make a dictionary for the skew values
    the skew values are the dictionary keys, and the values in the dictionary are arrays 
    of the positions where those skews are found in the genome
    """
    skew_values=CalculateGenomeSkew(genome)
    skew_dict={}
    lowest_skew=0
    for i in range(len(skew_values)):
        if skew_values[i] in skew_dict.keys():
            skew_dict[skew_values[i]].append(i)
        else:
            skew_dict[skew_values[i]]=[i]
    
        if skew_values[i] < lowest_skew:
            lowest_skew=skew_values[i]
    return skew_dict[lowest_skew]


def CalculateGenomeSkew(genome):
    skew_array=[0] #start with a 0 so that the indexing system works like you would count in the genome
    skew=0
    for i in range (len(genome)):
        if (genome[i] == 'A') or (genome[i] == 'T'):
            pass
        elif genome[i] == 'G':
            skew= skew+1
        elif genome[i] =='C':
            skew=skew-1
        else:
            print('unpermitted character.')
        skew_array.append(skew)
    return skew_array
genome_file=open('dataset_30277_10.txt','r')
genome=genome_file.readline()
genome_file.close()

FindOri(genome)
