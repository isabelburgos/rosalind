dnaseq = open("rosalind_prot.txt","r")
seq = str(dnaseq.read()).strip("\n")

table = open("proteintable.txt")
dic = {}
for line in table:
    line = (line.strip()).split()
    for i in range(0,len(line),2):
        codon,aa = line[i:i+2]
        dic[codon] = aa

codons = [seq[i:i+3] for i in range(0, len(seq), 3)]

protein = ""
for codon in codons:
    protein += dic.get(codon)

print(protein.strip("Stop"))
