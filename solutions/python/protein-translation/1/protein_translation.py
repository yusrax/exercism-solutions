"""Protein Translation"""
def proteins(strand):
    """Translate a given RNA sequence into proteins"""
    amino_acids = {
        "AUG": "Methionine",
        "UUU": "Phenylalanine",
        "UUC": "Phenylalanine",
        "UUA": "Leucine",
        "UUG": "Leucine",
        "UCU": "Serine",
        "UCC": "Serine",
        "UCA": "Serine",
        "UCG": "Serine",
        "UAU": "Tyrosine",
        "UAC": "Tyrosine",
        "UGU": "Cysteine",
        "UGC": "Cysteine",
        "UGG": "Tryptophan",
        "UAA": "STOP",
        "UAG": "STOP",
        "UGA": "STOP",
    }
    codons = [ strand[index:index+3] for index in range(0, len(strand), 3)]
    translation = []

    for codon in codons:
        if amino_acids[codon] == "STOP":
            break;
            
        translation.append(amino_acids[codon])

    return translation
