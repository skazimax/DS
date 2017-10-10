from itertools import permutations
a='ростелеком'
b=set()
c=set()
for x in range(3,len(a)+1):
    for comb in permutations(a,x):
        b.add(",".join(comb).replace(",",""))

with open("dic.txt","r") as f:
    for line in f:
        line=line.strip()
        c.add(line)
        