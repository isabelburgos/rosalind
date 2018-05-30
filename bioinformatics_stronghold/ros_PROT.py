dnaseq = open("rosalind_prot.txt","r")
seq = str(dnaseq.read()).strip("\n")

file = open("proteintable.txt")
dic = {}
for line in file:
    for val in line.split(" "):
        entry = val.strip("\n")
        if len(entry) == 0:
            pass
        if len(entry) == 3:
            name = entry
            dic.update({name:""})
        else:
            dic[name] += entry

codons = [seq[i:i+3] for i in range(0, len(seq), 3)]

protein = ""
for codon in codons:
    protein += dic.get(codon)

print(protein.strip("Stop"))
