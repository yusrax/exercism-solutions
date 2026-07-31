"""Hamming"""
def distance(strand_a, strand_b):
    """Calculate the Hamming distance between two DNA strands"""
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
        
    hamming_distance = 0
    for key, letter in enumerate(strand_a):
        if letter != strand_b[key]:
            hamming_distance += 1

    return hamming_distance
        