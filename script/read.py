with open("instance.txt") as f:
    lines = list(map(str.rstrip, f.readlines()))
    metadatas = lines[0].split(' ')
    N = int(metadatas[1])
    datas = list(map(lambda x:x.split(' '), lines[1:1+N]))
    trucs = []
    for data in datas:
        truc = (int(data[1]), int(data[3]))
        trucs.append(truc)

print(N)
print(trucs)
