seq = input("Sequence: ")

def dna_complement(seq):
    rev = seq[::-1]
    pairs = {
        "A": "T",
        "T": "A",
        "G": "C",
        "C": "G"
    }
    rev_comp = []
    for nuc in rev:
        comp = pairs.get(nuc)
        rev_comp.append(comp)
    dna_comp = "".join(rev_comp)
    return dna_comp

print(dna_complement(seq))
