file = open("rosalind_ins.txt")
lines = []
for line in file:
    clean = line.strip("\n")
    lines.append(clean.split(" "))
array = lines[1]
global swaps
swaps = 0

for i in range(1,len(array)):
    k = i
    while k > 0 and int(array[k]) < int(array[k-1]):
        array[k], array[k-1] = array[k-1], array[k]
        swaps += 1
        k -= 1

print(swaps)
