file = open("rosalind_cons.txt")
seqs = []
n = -1
for line in file:
    if line.startswith(">"):
        n += 1
        seqs.append("")
    else:
        seqs[n] += line.strip("\n")

matrix = [[],[],[],[]]

for n in range(0,len(seqs[0])):
    for i in range(0,4):
        matrix[i].append(0)

for seq in seqs:
    for n in range(0,len(seq)):
        if seq[n] == "A":
            matrix[0][n] += 1
        if seq[n] == "C":
            matrix[1][n] += 1
        if seq[n] == "G":
            matrix[2][n] += 1
        if seq[n] == "T":
            matrix[3][n] += 1

cons = ""

for n in range(0,len(seqs[0])):
    vals = []
    for i in range(0,4):
        vals.append(matrix[i][n])
    if vals[0] == max(vals):
        cons += "A"
    elif vals[1] == max(vals):
        cons += "C"
    elif vals[2] == max(vals):
        cons += "G"
    elif vals[3] == max(vals):
        cons += "T"

print(cons)
print("A:", " ".join(str(x) for x in matrix[0]))
print("C:", " ".join(str(x) for x in matrix[1]))
print("G:", " ".join(str(x) for x in matrix[2]))
print("T:", " ".join(str(x) for x in matrix[3]))
