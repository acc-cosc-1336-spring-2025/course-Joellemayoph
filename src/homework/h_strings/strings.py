#
def get_hamming_distance(dna1, dna2):

    count = 0 

    for i in range(len(dna1)):
        if dna1.upper()[i] != dna2.upper()[i]:
        
            count+=1
    return count


def get_dna_complement1(dna1, dna2):
    
    count = 0
    for i in range(len(dna1)):
        if dna1.upper()[i] == 'A' and dna2.upper()[i] == 'T':
            count += 1
        elif dna1.upper()[i] == 'T' and dna2.upper()[i] == 'A':
            count += 1
        elif dna1.upper()[i] == 'G' and dna2.upper()[i] == 'C':
            count += 1 
        elif dna1.upper()[i] == 'C' and dna2.upper()[i] == 'G':
            count += 1 

    return count

def get_dna_complement(dna):

    dna_comp = ''
    for i in range(len(dna)-1, -1, -1):
        if dna.upper()[i] == 'A':
            dna_comp += 'T'
            
        elif dna.upper()[i] == 'T':
            dna_comp += 'A'
         
        elif dna.upper()[i] == 'G':
            dna_comp += 'C'
         
        elif dna.upper()[i] == 'C':
            dna_comp += 'G'

    return dna_comp
        