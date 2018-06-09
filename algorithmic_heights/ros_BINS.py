file = open("rosalind_bins.txt")
lines = []
for line in file:
    clean = line.strip("\n")
    lines.append(clean.split(" "))
n = int(lines[0][0])
m = int(lines[1][0])
array = lines[2]
list = lines[3]

def binary_search(array,num):
    start = 0
    end = len(array) - 1
    found = False
    while start<=end and not found:
        midpt = (start+end)//2
        if int(array[midpt]) == num:
            index.append(midpt+1)
            found = True
        else:
            if num < int(array[midpt]):
                end = midpt - 1
            else:
                start = midpt + 1
    return found

index = []

for num in list:
    if binary_search(array,int(num)) == True:
        pass
    elif binary_search(array,int(num)) == False:
        index.append(-1)

print(" ".join(str(x) for x in index))
