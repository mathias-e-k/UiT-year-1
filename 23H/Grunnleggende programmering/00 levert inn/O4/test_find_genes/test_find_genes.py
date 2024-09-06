from Exercise05_06Extra_fn_as_function import find_genes
import unittest

# The only thing i had to change in my find_genes function is to make it return a list instead of a string

class Test_find_genes(unittest.TestCase):

    def test_sample1(self):
        # Samples from the original find genes task
        self.assertEqual(find_genes("TTATGTTTTAAGGATGGGGCGTTAGTT"), ["TTT", "GGGCGT"])

    def test_sample2(self):
        # Samples from the original find genes task
        self.assertEqual(find_genes("TGTGTGTATAT"), ["No genes found"])

    def test_one_gene(self):
        self.assertEqual(find_genes("AATGCGCCCATAA"), ["CGCCCA"])

    def test_multiple_genes(self):
        self.assertEqual(find_genes("CATCATGCCCTAAATGCGCTGA"), ["CCC", "CGC"])

    def test_no_genes(self):
        self.assertEqual(find_genes("CATGTATGGCTATTATGTTTCTCGAAGGAA"), ["No genes found"])
    
    def test_bad_input(self):
        self.assertEqual(find_genes("INVALID INPUT AAA!"), ["No genes found"])
    
    def test_gene_without_ending(self):
        self.assertEqual(find_genes("ATGCCCCCC"), ["No genes found"])

    def test_gene_not_multipleof3(self):
        self.assertEqual(find_genes("ATGCCCCTAG"), ["No genes found"])

    def test_no_ATG_in_genome(self):
        self.assertEqual(find_genes("CCCTAACCCTAGCCCTGACCCCCC"), ["No genes found"])
    
    def test_gene_length_0(self):
        self.assertEqual(find_genes("ATGTAATGATGTAG"), ["No genes found"])

    def test_gene_contains_ATG(self):
        self.assertEqual(find_genes("ATGCCATGCCCCTAA"), ["No genes found"])

    def test_gene_with_ATGA(self):
        # read ATGA.txt for info.
        self.assertEqual(find_genes("ATGCGATGACTTAA"), ["CGA", "ACT"])
    
    def test_ATGA2(self):
        # read ATGA.txt for info.
        self.assertEqual(find_genes("ATGACCCCCTAATGTAT"), ["ACCCCC"])
    
if __name__ == "__main__":
    unittest.main()