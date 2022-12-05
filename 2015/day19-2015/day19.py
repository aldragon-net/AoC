lines = []            
with open('day19input.txt', 'r') as inpfile:
    while True:
        line = inpfile.readline().strip()
        if line == '':
            line = inpfile.readline().strip()
            lines.append(line)
            break
        lines.append(line)
        
reactions = {}        
for line in lines:
    if not line.find('=>') == -1:
        comp = line.split('=>')[0].strip()
        prod = line.split('=>')[1].strip()
        if not comp in reactions:
            reactions[comp] = []
        prods = reactions[comp]
        prods.append(prod)
        reactions[comp] = prods

reverse = {}
for line in lines:
    if not line.find('=>') == -1:
        comp = line.split('=>')[1].strip()
        prod = line.split('=>')[0].strip()
        reverse[comp] = prod


molecule = lines[-1]
        
print(reactions)
print(reverse)
print(molecule)


products = []
for comp in reactions.keys():
    for i in range(len(molecule)):
        x = len(comp)
        if molecule[i:i+x] == comp:
            for prod in reactions[comp]:
                product = molecule[0:i]+prod+molecule[i+x:]
                products.append(product)
             
print('There are products: ', (len(products)))
unique = set(products)
print('There are unique products: ', (len(unique)))

input()

solutions = []
    
def revershrink(molecule, steps):
    print(molecule)
    if molecule == 'e':
        print('Solution found! required steps:', steps)
        solutions.append(steps)
        return
    for comp in reverse.keys():
        for i in range(len(molecule)):
            x = len(comp)
            if molecule[i:i+x] == comp:
                    prod = reverse[comp]
                    prevmol = molecule[0:i]+prod+molecule[i+x:]
                    revershrink(prevmol, steps+1)
    return
    
revershrink(molecule, 0)

print(solutions)

   
    
