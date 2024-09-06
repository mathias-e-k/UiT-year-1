import find_genes_v3
import random
GENOME_LENGTH = 200
letters = ["A", "C", "G", "T"]
genome = ""
for i in range(GENOME_LENGTH):
    genome += letters[random.randint(0, 3)]
genes = find_genes_v3.find_genes(genome)
if genes:
    gene_list = genes.split(",") # split the return value into list
    # print(len(gene_list))
    for gene in gene_list:
        print(f"{gene}")
else:
    print("no gene is found")

'''
Enter a genome string: ATGCTCTAATGTAACCCTGATGACATAG
CTC
ACA
<end>

Enter a genome string: CATGCCCCCATGACGGGTGTCTAG
CCCCCA
ACGGGTGTC
<end>

Enter a genome string: ATGACCCCCTAATGTAT
ACCCCC
<end>

Enter a genome string: ATGCGATGACTTAA
CGA
ACT
<end>
'''
