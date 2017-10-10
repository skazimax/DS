from itertools import combinations
a='ростелеком'
b=[]
for x in range(3,len(a)+1):
    for comb in combinations(a,x):
        b.append(",".join(comb).replace(",",""))