file1 = open("rosalind_orf.txt","r")
seq = ""
for line in file1:
    if not line.startswith(">"):
        seq += line.strip("\n")

file2 = open("proteintable.txt")
dic = {}
for line in file2:
    for val in line.split(" "):
        entry = val.strip("\n")
        if len(entry) == 0:
            pass
        if len(entry) == 3:
            name = entry.replace("U","T")
            dic.update({name:""})
        else:
            dic[name] += entry

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

rev_seq = dna_complement(seq)

proteins = []
def search(seq):
    for i in range(0,len(seq)-3):
        if seq[i:i+3] == "ATG":
            translate(seq,i)

def translate(seq,n):
    protein = ""
    for i in range(n, len(seq)-3, 3):
        if dic.get(seq[i:i+3]) == "Stop":
            proteins.append(protein)
            return
        else:
            protein += dic.get(seq[i:i+3])

search(seq)
search(rev_seq)
print("\n".join(set(proteins)))
