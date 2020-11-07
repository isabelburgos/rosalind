file = open("rosalind_revp.txt")
seq = ""
for line in file:
    if not line.startswith(">"):
        seq += line.strip("\n")

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

for s in range(0,len(seq)-3):
    for n in range(4,13):
        if s+n <= len(seq):
            subseq = str(seq[s:s+n])
            if subseq == dna_complement(subseq):
                print (str(s+1) + " " + str(n))
