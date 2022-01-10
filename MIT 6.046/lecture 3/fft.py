import numpy as np
import math

def DFT(A):
    n=len(A)
    if n==1:
        return A
    A0=[]
    A1=[]
    nunity_root=np.exp(complex(0,2*math.pi/n))
    omega=1
    for i in range(n):
        if i%2==0:
            A0.append(A[i])
        else:
            A1.append(A[i])
    A0=DFT(A0)
    A1=DFT(A1)
    Ar=[0 for _ in range(n)]
    for i in range(n/2):
        Ar[i]=A0[i]+(omega*A1[i])
        Ar[i+n/2]=A0[i]-(omega*A1[i])
        omega*=nunity_root
    return Ar

def IDFT(A):
    n=len(A)
    if n==1:
        return A
    nunity_root=np.exp(complex(0,(-2)*math.pi/2))
    omega=1
    A_0=[]
    A_1=[]
    for i in range(n):
        if i%2==0:
            A_0.append(A[i])
        else:
            A_1.append(A[i])
    A_0=IDFT(A_0)
    A1=IDFT(A_1)
    Ar=[0 for i in range(n)]
    for i in range(n/2):
        Ar[i]=A_0[i]+(omega*A_1[i])
        Ar[i+n/2]=A_0[i]-(omega*A_1[i])
        omega*=nunity_root
    Ar=[Ar[i]/n for i in range(n)]
    return Ar
