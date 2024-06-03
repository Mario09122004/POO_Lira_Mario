a = {1,5,2,8,4}
b = {3,6,8,4,2,67}
c = {3,6,8,4,6}

pares = {0}

for x in a:
    if x%2==0:
        pares.add(x)

for x in b:
    if x%2==0:
        pares.add(x)

for x in c:
    if x%2==0:
        pares.add(x)

pares.remove(0)
print(pares)