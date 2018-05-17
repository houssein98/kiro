import numpy as np
import random
import itertools

def permute(liste):
    for i in range(len(liste)):
        A = liste[i]
        j = random.randint(0,len(liste)-1)
        B = liste[j]
        liste[i]= B
        liste[j]= A
        return liste
    
with open("instance_L.in") as f:
    lines = list(map(str.rstrip, f.readlines()))
    metadatas = lines[0].split(' ')
    nV = int(metadatas[1])
    nA = int(metadatas[3])
    nP = int(metadatas[5])
    B = int(metadatas[7])
    K = int(metadatas[9])
    G = int(metadatas[11])
    datas = list(map(lambda x:x.split(' '), lines[1:1+nV+nA]))
    datasV = datas[:nV]
    datasA = datas[nV:1+nV+nA]
    A, V = [], []
    for data in datasV:
        vol = [int(data[1])]+[int(data[i]) for i in range(3,3+nP)]
        V.append(vol)
    for data in datasA:
        arc = (int(data[1]), int(data[3]), int(data[5]), int(data[7]), int(data[9]))
        A.append(arc)
        
#print(nV,nA,nP,B,K,G)
#print(V)
#print(A)

MI= np.zeros((nV,nV))
for a in A:
    if a[3]==0:
        MI[a[1]-1,a[2]-1]=1;
    else: 
        MI[a[1]-1,a[2]-1]=-1;

#print(MI)

vol_depart = [];
for j in range(nV):
    if np.array_equal(MI[:,j],np.zeros(nV)):
        vol_depart.append(j+1)

    
def cout1(R):
    C=0
    for p in range(len(R)):
        for v in R[p]:
            C+= V[v-1][p+1];
    return C

def cout2(r) :
    V=[]
    for v in r :
        for k in range(1,len(r)) :
            
            for i in range(0,k) :
                test=0
                somme=0
                for j in range(i,k) :
                    for arc in A :
                        if arc[3]==0 and arc[1]==r[j] :
                            test+=1
                        somme+=arc[4]
                if v==r[k] and test==0 and somme>=K :
                    V+=[v]
    a = len(V);
    return(a*G)

def rotation_cost(r,p) : #ne pas oublier la maintenance
    res=0;
    for v in r:
        res+=V[v-1][p+1];
    res+=cout2(r);
    return(res)

def cost(R) :
    res=0;
    for p in range(nP) :
        res+=rotation_cost(R[p],p)
    for v in V:
        n=0;
        for r in R :
            for i in r :
                if v[0]==i :
                    n+=1;
        #res+=B*abs(n-1);
    return (res)


    
def solution(M, volsInitiaux): 
    avions = []
    M2=np.zeros((nV,nV))
    for i in range(nV):
        for j in range(nV):
            M2[i,j]=M[i,j]
            
    for i in range(nP):
        l = []
        a = random.randint(0,nV-1)
        l.append(a+1)
        while(True):
            J = [i  for i in range(nV)]
            permute(J)
            for j in J:
                if(M2[a,j] == -1 or M2[a,j] == 1):
                    l.append(j+1)
                    M2[:,j] = 0
                    a = j
                    break
            if np.array_equal(M2[a,:],np.zeros(nV)):
                break
        avions.append(l)
        

    return avions

R = solution(MI,vol_depart)

# permutation de seq


min=cost(R)
print(min)

for i in range(100):
    R2 = solution(MI,vol_depart)
    c = cost(R2)
    print(c,min)
    if c<min:
        R=R2
        min = c
        
for i in range(10):  
    R = permute(R)
    if cost(R)<min:
        print(i)
        min=cost(R)
        with open("solutionL1.in", 'w') as f:
            for p, r in enumerate(R):
                p = p+1
                f.write('p {} a '.format(p))
                for i in r:
                    f.write('{} '.format(i))
                f.write('\n') 
            
        
        print(cost(R))
