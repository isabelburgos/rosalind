#extract sequences from file
file = open("rosalind_lcsm.txt")
seqs = []
n = -1
for line in file:
    if line.startswith(">"):
        n += 1
        seqs.append("")
    else:
        seqs[n] += line.strip("\n")

#separate shortest sequence from other sequences
shortest_seq = min(seqs, key=len)
seqs.remove(shortest_seq)

#break shortest sequence into all possible subsequences with a specific range of lengths
def break_seq(x):
    raw_subseqs = []
    for n in range(x,x+3):
        for i in range(0,len(shortest_seq) - len(shortest_seq)%n):
            raw_subseqs.append(shortest_seq[i:i+n])
    subseqs = sorted(set(raw_subseqs),key = len)[::-1]
    return subseqs

#determine if a subsequence is in a sequence
def match(seq,subseq):
    if subseq in seq:
        return True
    else:
        return False

#go through set of subsequences (longest to shortest), stop once a subsequence is found in all sequences
def search(seqs,subseqs,found):
    if found == True:
        pass
    else:
        for subseq in subseqs:
            if all(match(seq,subseq) == True for seq in seqs):
                global lcsm
                lcsm = subseq
                found = True
                return True

#to make code more efficient, divide subsequences into smaller sets
#start with 2bp, test within ranges of 3bp
def triage(n):
    subseq_set = break_seq(n)
    if search(seqs,subseq_set,False) == True:
        #if a common subsequence is found in one set, move onto testing longer subsequences
        triage(n+3)
    else:
        #stop once no common sequence is found in a set of subsequences
        pass

triage(2)
print(lcsm)
#return the most recent common subsequence, which is the longest
