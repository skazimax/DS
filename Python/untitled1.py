def matrix():
    M=input("matrix: ")
    col=M.count(";")+1
    M=M.replace(";",",").split(",")
    try:
        M=list(map(int,M))
        m=[M[x:x+col]for x in range(0,len(M),col)]
        if col**2!=len(M):
            print("Not a quadratic matrix")
        else:
            print(str(m).replace("],","]\n"))
            return m
    except:
        print("Input error")
    

def det(x):
    if x==None:
        return
    else:
        if len(x[0])==2:
            d=x[0][0]*x[1][1]-x[0][1]*x[1][0]
            return d
        else:
            d=0
            for i in range(len(x[0])):
                d1=[]
                for j in range(1,len(x[0])):
                    d1.append([el for k, el in enumerate(x[j]) if k not in [i]])
                #print("d1"+str(d1))
                d+=x[0][i]*(-1)**(2+i)*det(d1)
                return d
            
print("Determinant: "+str(det(matrix())))