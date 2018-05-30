file = open("rosalind_gc.txt")
dic = {}
for line in file:
    if line.startswith(">"):
        name = line.strip(">\n")
        dic.update({name:""})
    else:
        dic[name] += line.strip("\n")

def GC_cont(seq):
    return ((seq.count("G") + seq.count("C"))/len(seq))

for name in dic:
    seq = dic.get(name)
    dic.update({name:GC_cont(seq)})

max_gc = max(dic.keys(), key=(lambda k: dic[k]))
print(max_gc)
print(format(dic.get(max_gc)*100, '.6f'))
