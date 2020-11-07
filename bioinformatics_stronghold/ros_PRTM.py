table = open("masstable.txt")
masstable = {}
for row in table:
    vals = row.strip("\n").split("   ")
    masstable.update({vals[0]:float(vals[1])})

total_mass = 0

file = open("rosalind_prtm.txt")
seq = str(file.read()).strip("\n")

for letter in seq:
    total_mass += masstable.get(letter)

print(round(total_mass,3))
