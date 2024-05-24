calificacion1 = float(input("Ingresa la primera promedio: "))
calificacion2 = float(input("Ingresa la segunda promedio: "))
calificacion3 = float(input("Ingresa la tercera promedio: "))

if calificacion1>calificacion2 and calificacion1>calificacion2:
    print("La mayor promedio es de: ",calificacion1)
elif calificacion2>calificacion1 and calificacion2>calificacion3:
    print("La mayor promedio es de: ",calificacion2)
elif calificacion3>calificacion1 and calificacion3>calificacion1:
    print("La mayor promedio es de: ",calificacion3)
else:
    print("Se repiten las capromedio")