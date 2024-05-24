calificacion1 = float(input("Ingresa la primera calificación: "))
calificacion2 = float(input("Ingresa la segunda calificación: "))
calificacion3 = float(input("Ingresa la tercera calificación: "))

if calificacion1>calificacion2 and calificacion1>calificacion2:
    print("La mayor calificación es de: ",calificacion1)
elif calificacion2>calificacion1 and calificacion2>calificacion3:
    print("La mayor calificación es de: ",calificacion2)
elif calificacion3>calificacion1 and calificacion3>calificacion1:
    print("La mayor calificación es de: ",calificacion3)
else:
    print("Se repiten las calificaciones")