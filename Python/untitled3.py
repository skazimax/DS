from itertools import combinations
a='ростелеком'
b=[]
c=[]
for x in range(3,len(a)+1):
    for comb in combinations(a,x):
        b.append(",".join(comb).replace(",",""))
        
a=0
with open("dic.txt","r") as f:
    for line in f:
        line=line.strip()
        if line in b:
            a+=1
            print(line)
print(a)