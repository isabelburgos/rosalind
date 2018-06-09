import urllib.request

dic = {}
file = open("rosalind_mprt.txt")
for entry in file:
    name = entry.strip("\n")
    dic.update({name:""})
    with urllib.request.urlopen("http://www.uniprot.org/uniprot/" + name + ".fasta") as response:
      html = str(response.read())
    data = html.split("\\n")
    for line in data:
        if ">" in line:
            pass
        else:
            dic[name] += line

dic2 = {}
for name in dic:
    dic2.update({name:""})
    seq = dic.get(name)
    for n in range(0,len(seq)-3):
        if seq[n] == "N":
            if not seq[n+1] == "P":
                if seq[n+2] == "S" or seq[n+2] == "T":
                    if not seq[n+3] == "P":
                        dic2[name] += str(n+1) + " "
for name in dic2:
    if dic2.get(name) == "":
        pass
    else:
        print(name)
        print(dic2.get(name))
