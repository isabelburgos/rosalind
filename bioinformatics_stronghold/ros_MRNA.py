protein = open("rosalind_mrna.txt","r")
seq = str(protein.read()).strip("\n")

file = open("proteintable.txt")
AAs = []
#extracting amino acids from codon table
for line in file:
    for val in line.split(" "):
        entry = val.strip("\n")
        if len(entry) == 1:
            AAs += entry

dic = {}
for AA in AAs:
    dic.update({AA:AAs.count(AA)})

combos = 3 #3 possible stop codons

for AA in seq:
    combos = combos*dic.get(AA)
print(combos%1000000)
