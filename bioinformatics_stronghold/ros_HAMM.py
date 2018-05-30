s = input("s: ")
t = input("t: ")
mut = 0

for n in range(0,len(s)):
    if s[n] != t[n]:
        mut += 1

print(mut)
