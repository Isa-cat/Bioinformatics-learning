import numpy as np
"""
To find the frequency of a given word (=base k-mer) in a genomic sequence: A sequence and k (length of k-mer) is given to the FrequentWords function, which creates an 
empty list for alter. It also calls the FrequencyTable function to create a dictionary of the frequency of each base sequence of length k in the text. MaxMap will then find the 
highest frequency as saved in the dictionary, and the list of k-mers is compared against the highest frequency value: all k-mers that occur at that frequency are added to
the list of frequent words and finally, printed.
"""
def FrequentWords(text, k):
    frequent_words = []
    freq_map=FrequencyTable(text, k)
    max_freq = MaxMap(freq_map)
    #print(max_freq)
    for key in freq_map:
        if freq_map[key] == max_freq:
            #print(key)
            frequent_words.append(key)
    return frequent_words

def FrequencyTable(text,k):
    freq_dict={}
    for i in range (len(text)-k+1):
        key=str(text[i:i+k])
        if key in freq_dict.keys():
            freq_dict[key]= freq_dict[key]+1
        else:
            freq_dict[key]=1
        #print(text[i:i+k])
    print(freq_dict)
    return freq_dict

def MaxMap(dict_word_frequency):
    return max(dict_word_frequency.values())

FrequentWords('TGGAGGTAACCTTGTGGAGGTACGGTGAGTGGAGGTTGGAGGTAACCTTGACGGTGAGTGGAGGTAACCTTGCTGATACATAACCTTGAACCTTGTGGAGGTCTGATACATCTGATACATCTGATACATTGGAGGTGTATATTCACGGTGAGACGGTGAGACGGTGAGCTGATACATTGGAGGTTGGAGGTGTATATTCAACCTTGGTATATTCTGGAGGTAACCTTGGTATATTCCTGATACATCTGATACATCTGATACATAACCTTGACGGTGAGTGGAGGTTGGAGGTCTGATACATACGGTGAGACGGTGAGTGGAGGTAACCTTGTGGAGGTACGGTGAGGTATATTCGTATATTCGTATATTCTGGAGGTGTATATTCGTATATTCAACCTTGCTGATACATACGGTGAGCTGATACATACGGTGAGTGGAGGTGTATATTCCTGATACATAACCTTGACGGTGAGACGGTGAGCTGATACATAACCTTGGTATATTCGTATATTCGTATATTCAACCTTGAACCTTGGTATATTCACGGTGAGCTGATACATTGGAGGTTGGAGGTGTATATTCACGGTGAGGTATATTCCTGATACATAACCTTGCTGATACATACGGTGAGAACCTTGAACCTTGCTGATACATCTGATACATAACCTTGGTATATTCGTATATTCAACCTTGAACCTTGCTGATACATTGGAGGTACGGTGAGAACCTTGGTATATTCAACCTTGTGGAGGTTGGAGGTGTATATTCTGGAGGTAACCTTGCTGATACATCTGATACATGTATATTCGTATATTCGTATATTCTGGAGGTTGGAGGTTGGAGGTAACCTTG', 12)
