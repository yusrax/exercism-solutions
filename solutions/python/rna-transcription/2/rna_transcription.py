"""Determine RNA complement"""
def to_rna(dna_strand):
    """Trancribe given DNA to RNA"""
    complement = {
        "C": "G",
        "G": "C",
        "T": "A",
        "A": "U",
    }

    return "".join(complement[nucleotide] for nucleotide in dna_strand)
        
