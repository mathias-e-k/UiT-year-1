def find_genes(genome: str) -> str:
    genes = ""
    for _ in range(genome.count("ATG")):
        genome = genome.partition("ATG")[2]

        if genome.partition("TAG")[1]:
            gene1 = genome.partition("TAG")[0]
        else: gene1 = ""

        if genome.partition("TAA")[1]:
            gene2 = genome.partition("TAA")[0]
        else: gene2 = ""
        
        if genome.partition("TGA")[1]:
            gene3 = genome.partition("TGA")[0]
        else: gene3 = ""

        for gene in [gene1, gene2, gene3]:
            if len(gene) % 3 != 0:
                continue

            if len(gene) == 0:
                continue

            if "ATG" in gene or "TAG" in gene or "TAA" in gene or "TGA" in gene:
                continue

            genes += gene + ","
            
    return genes[:-1]


if __name__ == "__main__":
    user_input = input("Enter a genome string: ")
    genes = find_genes(user_input)
    if genes:
        gene_list = genes.split(",")
        for gene in gene_list:
            print(gene)
    else:
        print("no gene is found")

            