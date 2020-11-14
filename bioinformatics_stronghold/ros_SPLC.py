file = open("rosalind_splc.txt")
seqs = []
n = -1
for line in file:
    if line.startswith(">"):
        n+=1
        seqs.append("")
    else:
        seqs[n] += line.strip("\n")

table = open("proteintable.txt")
dic = {}
for line in table:
    for val in line.split(" "):
        entry = val.strip("\n")
        if len(entry) == 0:
            pass
        if len(entry) == 3:
            name = entry
            dic.update({name:""})
        else:
            dic[name] += entry

def search_find(seq,intr):
    loc = seq.find(intr)
    if loc == -1:
        return(seq)
    else:
        seq = seq[0:loc] + seq[loc+len(intr):]
        newseq = search_find(seq,intr)
        return(newseq)

dna = seqs[0]
for intr in seqs[1:]:
    dna = "".join((search_find(dna,intr)))


codons = [dna[i:i+3] for i in range(0, len(dna), 3)]
protein = ""
for codon in codons:
    c = codon.replace("T","U")
    protein += dic.get(c)

print(protein.strip("Stop"))
