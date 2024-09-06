def find_genes(genome: str) -> str:
    # does not work properly if genome has "ATGA"
    genes = ""
    triplet = ""
    gene_start = -1
    for i in range(len(genome)-2):
        triplet = genome[i:i+3]

        if triplet == "ATG":
            gene_start = i+3

        if gene_start == -1:
            continue

        if triplet in ["TAG", "TAA", "TGA"]:
            gene_end = i

            gene = genome[gene_start:gene_end]
            gene_start = -1
            if len(gene) % 3 == 0 and len(gene) > 0:
                genes += gene + ","

    if genes == "":
        return "no gene is found"
    return genes[:-1]


if __name__ == "__main__":
    user_input = input("Enter a genome string: ").strip().upper()
    gene_list = find_genes(user_input).split(",")
    for gene in gene_list:
        print(gene)
