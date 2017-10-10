
import numpy as np

def m_det(x):
    if x.shape==(2,2):
        m=x[0,0]*x[1,1]-x[0,1]*x[1,0]
        return m
    
    else:
        m=0
        for i in range(len(x)):
            m+=x[0,i]*(-1)**(2+i)*m_det(np.delete(np.delete(x,0,0),i,1))
        return m


def mat():
    test=input("matrix: ")
    row=test.count(";")
    test=test.replace(";",",").split(",")
    try:
        t2=list(map(int,test))
    except:
        print("Wrong input")
    else:
        t2=np.array(t2)
        try:
            t2=t2.reshape(row+1,row+1)
            print("Your matrix is:"+"\n"+str(t2))
            det=m_det(t2)
            print("Determinant:"+str(det))
        except:
            print("not a quadratic matrix")
        
    
    
   