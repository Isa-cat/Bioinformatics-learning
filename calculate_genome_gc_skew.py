def CalculateGenomeSkew(genome):
    skew_string='0 '
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
        skew_string=skew_string+str(skew)+' '  
    return skew_string

CalculateGenomeSkew('GAGCCACCGCGATA')
            
