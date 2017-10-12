import random as rd
m1=[]
m2=[]
rm1_col=0
rm1_row=-1
rm2_col=-2
rm2_row=0
while rm1_row!=rm2_col:
    rm1_col=rd.randint(1,9)
    rm1_row=rd.randint(1,9)
    rm2_row=rd.randint(1,9)
    rm2_col=rd.randint(1,9)
print(rm1_col,rm1_row,rm2_col,rm2_row)

for i in range(rm1_col):
    rm1_=[]
    for j in range(rm1_row):
        rm1_.append(rd.randint(0,99))
    m1.append(rm1_)
    
for i in range(rm2_col):
    rm2_=[]
    for j in range(rm2_row):
        rm2_.append(rd.randint(0,99))
    m2.append(rm2_)    
print("Matrix 1:\n"+str(m1).replace("],","]\n")+"\n")
print("Matrix 2:\n"+str(m2).replace("],","]\n")+"\n")
    

def mm(m1,m2):
    if len(m1[0])==len(m2):
        mm1=[]
        for i in range(len(m1)):
            mm=[]
            for j in range(len(m2[0])):
                s=0
                for k in range(len(m1[0])):
                    s+=m1[i][k]*m2[k][j]
                mm.append(s)
            mm1.append(mm)
        print("Determinant M1 x M2:\n"+str(mm1).replace("],","]\n"))
                    
mm(m1,m2)
