trucs = [(2, 3), (5, 7)]

with open("solution.txt", 'w') as f:
    for i, truc in enumerate(trucs):
        x, y = truc
        f.write('i {} x {} y {}\n'.format(i, x, y)) # ATTENTION AU \n
