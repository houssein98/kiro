import numpy as np
import random
import itertools


with open("instance_M.in") as f:
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
print(vol_depart)

    
def cout1(R):
    C=0
    for p in range(len(R)):
        for v in R[p]:
            C+= V[v-1][p+1];
    return C

def rotation_cost(r,p) : #ne pas oublier la maintenance
    res=0;
    for v in r:
        res+=V[v-1][p+1];
    return(res)
    
def cost(R) :
    res=0;
    for p in range(nP) :
        res+=rotation_cost(R[p],p)
    for v in V :
        n=0;
        for r in R :
            for i in r :
                if v==i :
                    n+=1;
        #res+=B*abs(n-1);
    return (res)


    
def solution(M, volsInitiaux): 
    avions = []
    for i in range(nP):
        l = []
        if i<len(volsInitiaux):
            a = volsInitiaux[i]-1
        else:
            a = random.randint(0,nV)
        l.append(a+1)
        while(True):
            for j in range(nV):
                if(M[a,j] == 1 or M[a,j] == -1):
                    l.append(j+1)
                    M[:,j] = 0
                    a = j
                    break
            if np.array_equal(M[a,:],np.zeros(nV)):
                break
        avions.append(l)
    return avions
R = solution(MI,vol_depart)

# permutation de seq
def permutliste(seq, er=False):
    p = [seq]
    n = len(seq)
    for k in range(0,n-1):
        for i in range(0, len(p)):
            z = p[i][:]
            for c in range(0,n-k-1):
                z.append(z.pop(k))
                if er==False or (z not in p):
                    p.append(z[:])



LR = list(itertools.permutations(R))
min=cost(R)
k=0
for i in range(len(LR)):
    if cost(LR[i])<min:
        k=i
        min=cost(LR[i])

print(cost(LR[k]))
with open("solutionM.in", 'w') as f:
    for p, r in enumerate(LR[k]):
        p = p+1
        f.write('p {} a '.format(p))
        for i in r:
            f.write('{} '.format(i))
        f.write('\n') 
