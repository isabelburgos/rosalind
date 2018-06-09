file = open("rosalind_deg.txt")
data = []
for line in file:
    clean = line.strip("\n")
    data.append(clean.split(" "))
specs = data[0]
del data[0]
index = [0] * int(specs[0])

for pair in data:
    for n in pair:
        index[int(n)-1] += 1
#you just need to count how many times a number appears in the data set to find its degree
#keeping the data pairs isn't actually necessary

print(" ".join(str(x) for x in index))
