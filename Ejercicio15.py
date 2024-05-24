while True:
    a = int(input("¿Cuántas edades se analizarán?: "))
    if a<8:
        print("Minimo 8 edades")
    else:
        break
edad = []
adulto = []
menor = []
for x in range(a):
    edad.append(int(input(f"Edad de la {x+1}ª persona: ")))
    #print(edad[x])
    if edad[x]>18:
        adulto.append(edad[x])
    else:
        menor.append(edad[x])


print("Todas las edades")
print("Edades de menor a mayor:", sorted(edad))
print("Edades de mayor a menor:", sorted(edad, reverse=True))

print("Mayores de edad")
print("Edades de menor a mayor:", sorted(adulto))
print("Edades de mayor a menor:", sorted(adulto, reverse=True))

print("Menores de edad")
print("Edades de menor a mayor:", sorted(menor))
print("Edades de mayor a menor:", sorted(menor, reverse=True))

