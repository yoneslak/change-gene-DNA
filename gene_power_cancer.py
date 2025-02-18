def dna_composition(gene_purpose):
    
    #composition purpose DNA nocluetid
    A = np.sum(gene_purpose == 'A')
    G = np.sum(gene_purpose == 'G')
    C = np.sum(gene_purpose == 'C')
    T = np.sum(gene_purpose == 'T')
    A_G = A,G
    T_C = T,C
    return A_G,T_C
def dna_cancer(gene_purpose):
    cancer = []
    for i in range(len(gene_purpose)):
        if gene_purpose[i] == 'A':
            cancer.append('ACAFA')
        elif gene_purpose[i] == 'G':
                cancer.append('GTFGG')
        elif gene_purpose[i] == 'C':
                    cancer.append('CGFC')
        elif gene_purpose[i] == 'T':
                        cancer.append('TATFFAT')
    return (cancer)
def change_dna(gene_purpose):
    change = []
    for i in range(len(gene_purpose)):
            if gene_purpose[i] == 'A':
                    change.append('T')
            elif gene_purpose[i] == 'C':
                    change.append('G')
            elif gene_purpose[i] == 'G':
                    change.append('A')
            elif gene_purpose[i] == 'T':
                    change.append('C')
    return(change)
 #Creating genes superior to human
import numpy as np
gene_char1 = ['A','G','C','T']
gene_char2 = ['G','C','A','T']
gene_lenght1 = 10
gene_lenght2 = 20
gene_randomizer1 = np.random.choice(gene_char1 , size = gene_lenght1)
gene_randomizer2 = np.random.choice(gene_char2 , size = gene_lenght2)
gene_array1 = np.array(gene_randomizer1)
gene_array2 = np.array(gene_randomizer2)

#purpose gene orginal
gene_purpose = np.concatenate((gene_randomizer1, gene_randomizer2))

#composition DNA
print("\ncomposition dna with other:\n",dna_composition(gene_purpose))
print("\ngene is healt without cancer:\n",gene_purpose)

#transformer DNA to cancer
cancer_dna = dna_cancer(gene_purpose)
print("\ngene is with cancer dna:\n",cancer_dna)

#change DNA 
change_gene = change_dna(gene_purpose)
print("\ngene is changed of orginal gene:\n",change_gene)

#visualation data
import matplotlib.pyplot as plt
plt.title('change_gene_orginal')
plt.bar(gene_purpose,change_gene)
plt.show()
plt.title('gene_cancer')
plt.bar(gene_purpose,cancer_dna)
plt.show()