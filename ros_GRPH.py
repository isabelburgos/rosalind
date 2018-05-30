file = open("rosalind_grph.txt")
dic = {}
for line in file:
    if line.startswith(">"):
        name = line.strip(">\n")
        dic.update({name:""})
    else:
        dic[name] += line.strip("\n")

for seq_name in dic.keys():
    seq = dic.get(seq_name)
    for seq2_name in dic.keys():
        seq2 = dic.get(seq2_name)
        if seq_name == seq2_name:
            pass
        elif seq[0:3] == seq2[-3::]:
            print(seq2_name,seq_name)
