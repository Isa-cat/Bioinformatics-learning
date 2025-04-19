#pattern_counter: count how often a specific pattern appears in a sequence
genome_file=open('Vibrio_cholerae.txt', 'r')
genome=genome_file.readline()
#readlines gave no output, guess cause it is only one line in there

def PatternIndices(pattern, sequence):
    """
    in theory, the counter would have to 'wrap' to also go from last character in string to the first ones to check
    that the pattern can not be completed that way?
        
    """
    length=len(pattern)
    indices=str()
    for i in range (len(sequence)-length+1): 
        if sequence[i:i+length] == pattern:
            indices = indices+str(i)+' '
        else:
            pass
    return indices

PatternIndices('CTTGATCAT', genome)
