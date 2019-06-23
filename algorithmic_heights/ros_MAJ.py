file = open("rosalind_maj.txt")
matrix = []
lines = file.read().split("\n")
for line in lines:
    if any(n.isdigit() for n in line):
        set = (list(line.split(" ")))
        matrix.append(set)

half = 0.5*int(matrix[0][1])

out = []
for i in range(1,len(matrix)):
    mode = (max({*matrix[i]},key = matrix[i].count))
    if matrix[i].count(mode) > half:
        out.append(mode)
    else:
        out.append("-1")

print(" ".join(out))
