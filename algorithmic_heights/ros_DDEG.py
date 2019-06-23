file = open("rosalind_ddeg.txt")
matrix = []
lines = file.read().split("\n")
for line in lines:
    if any(n.isdigit() for n in line):
        set = (list(map(int,line.split(" "))))
        matrix.append(set)

vert = matrix[0][0]

count = [0]*vert
dic = {}
for i in range(1,vert+1):
    dic.update({i:[]})

for set in matrix[1:len(matrix)]:
    dic[set[0]].append(set[1])
    dic[set[1]].append(set[0])
    for n in set:
        count[n-1] += 1

array = []
for n in dic:
    deg = 0
    for v in dic.get(n):
        deg += count[v-1]
    array.append(deg)

print(" ".join(map(str,(array))))
