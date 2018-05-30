seq = input("Sequence: ")
subseq = input("Subsequence: ")

locations = []

n = len(subseq)
for i in range(0,len(seq)):
    if seq[i:i+n] == subseq:
        locations.append(str(i+1))

print(" ".join(locations))
