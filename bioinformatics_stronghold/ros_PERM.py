n = int(input("n: "))
vals = list(range(1,n+1))

all_perms = []

def permute(perm):
    new_perms = []
    for val in vals:
        if val not in perm:
            new = []
            new += perm
            new.append(val)
            new_perms.append(new)
    for p in new_perms:
        if len(p) == len(vals):
            all_perms.append(p)
        else:
            permute(p)

for n in range(1,n+1):
    perm = [n]
    permute(perm)

print(len(all_perms))
for p in all_perms:
    print(" ".join(map(str,p)))
