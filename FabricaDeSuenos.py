print('------------PROGRAMA ASIGNACION DE PUNTOS------------')

puntos = int
puntos_ext = int
puntos_totales = int
porcen = float
cuota = int (input("Ingrese cuota : "))
venta = int (input("Ingresa la cantidad en ventas : "))
producto = input("Que tipo de producto vendio Galletas o Gomas :")
segmento =  input("Escriba el tipo de segmento Oro, Plata, Bronce ")



porcen = (100/cuota)*venta

if venta > cuota:
    if producto.upper() == "GOMAS":
        if segmento.upper() == "ORO":
            puntos = 234000
            print(f"Felicidades se le otorgaron {puntos}")
            if porcen >150:
                puntos_ext =20000
                print(f"Superaste el 150% de la cuota, con un porcentaje de {porcen}% , puntos extras {puntos_ext}")
                puntos_totales = puntos+puntos_ext
                print(f"El total de puntos son {puntos_totales}")
        else:
            print("Deberes realizar mas ventas para que puedas obtener puntos")
    elif producto.upper()== "GALLETAS":
        if segmento.upper() == "ORO":
            puntos = 15600
            print(f"Felicidades se le otorgaron {puntos}")
            if porcen >150:
                puntos_ext =30000
                print(f"Superaste el 150% de la cuota, con un porcentaje de {porcen}% , puntos extras {puntos_ext}")
                puntos_totales = puntos+puntos_ext
                print(f"El total de puntos son {puntos_totales}")
        elif segmento.upper()=="BRONCE":
            puntos = 120000
            print(f"Felicidades se le otorgaron {puntos}")
        else:
            print("Deberes realizar mas ventas para que puedas obtener puntos")
elif venta < cuota:
    if segmento.upper()== "PLATA":
        puntos = 1000
        print(f"Felicidades se le otorgaron {puntos}")
    else:
        print("Deberes realizar mas ventas para que puedas obtener puntos")
else:
    print("Deberes realizar mas ventas para que puedas obtener puntos")





#By ADRIAN



