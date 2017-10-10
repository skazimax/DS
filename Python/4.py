M=input("Matrix:\n")
col=M.count(";")+1
M=M.replace(";",",").split(",")
M=list(map(int,M))
m=[M[x:x+col]for x in range(0,len(M),col)]
print(str(m).replace("],","]\n"))
