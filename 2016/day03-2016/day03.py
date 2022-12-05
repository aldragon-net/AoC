triples = []
with open('day03input.txt', 'r') as inpfile:
    while True:
        line = inpfile.readline().strip()
        if line == '':
            break
        triple = [int(L.strip()) for L in line.split()]
        triples.append(triple)

def is_triangle(triple):
    a = triple[0]
    b = triple[1]
    c = triple[2]
    if (a+b>c) and (a+c>b) and (b+c>a):
        return True
    else:
        return False

n = 0
for triple in triples:
    if is_triangle(triple):
        n = n + 1

print('There are', n, 'triangles')
input()

n = 0
for i in range(len(triples)//3):
    for j in range(3):
        a = triples[i*3][j]
        b = triples[i*3+1][j]
        c = triples[i*3+2][j]
        if is_triangle([a,b,c]):
            n = n + 1
print('There are', n, 'triangles in 2nd notation')
input()