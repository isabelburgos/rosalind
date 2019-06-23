file = open("rosalind_mer.txt")
matrix = []
lines = file.read().split("\n")
for line in lines:
    if any(n.isdigit() for n in line):
        set = (list(map(int,line.split(" "))))
        matrix.append(set)

comb = sorted(matrix[1] + matrix[3])

print(" ".join(map(str,(comb))))
