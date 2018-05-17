with open("instance_exemple.in") as f:
    lines = list(map(str.rstrip, f.readlines()))
    metadatas = lines[0].split(' ')
    nV = int(metadatas[1])
    nA = int(metadatas[3])
    nP = int(metadatas[5])
    B = int(metadatas[7])
    K = int(metadatas[9])
    G = int(metadatas[11])
    datas = list(map(lambda x:x.split(' '), lines[1:1+nV+nA]))
    datasV = datas[1:nV]
    datasA = datas[nV:1+nV+nA]
    A, V = [], []
    for data in datasV:
        vol = (int(data[1]), int(data[3]), int(data[4]), int(data[5]))
        V.append(vol)
    for data in datasA:
        arc = (int(data[1]), int(data[3]), int(data[5]), int(data[7]), int(data[9]))
        A.append(arc)
        
print(nV,nA,nP,B,K,G)
print(V)
print(A)
