#"Eres un desarrollador junior en una empresa de software, y te han asignado la tarea de crear un
#usuario a través de la consola, solicitando cuatro datos esenciales: el nombre del producto, el
#precio unitario, la cantidad de productos adquiridos, y el porcentaje de descuento que se aplicará,
#si es que existe alguno. Es fundamental que el programa maneje adecuadamente las entradas,
#validando que tanto el precio como la cantidad sean números positivos, y que el descuento esté
#dentro del rango aceptable de 0 a 100%.
#Con estos datos, el programa debe calcular el costo total de la compra. Primero, debe determinar
#el costo sin aplicar ningún descuento y, luego, si corresponde, aplicar el descuento especificado
#para calcular el monto final. Además, este costo total debe ser mostrado junto con el nombre del
#producto, de manera clara y formateada, asegurando que el resultado sea fácil de interpretar, por
#ejemplo, presentando el valor con dos decimales.
#Es importante que consideres la estructura y legibilidad de tu código, asegurándote de que esté
#bien organizado y libre de errores. Por último, prueba el programa con distintos escenarios,
#incluyendo casos extremos, para garantizar que funcione correctamente en todas las situaciones
#posibles.

nameProduct=str()
productPrice=float()
quantityProducts=int()
discountPercentage=int()


print("Ingresa el nombre del producto")
nameProduct=str(input())
print("Ingrese el precio unitario del producto")
productPrice=float(input())

if productPrice>0:
    print("Ingresa la cantidad de productos adquiridos")
    quantityProducts=int(input())
else:
    print("Valor no es valido")
    
if quantityProducts>0:
    print("¿Que porcentaje de descuento tiene el producto?\n Digita un valor de 0 a 100\n Si el producto no tiene descuento digita el valor 0 ")
    discountPercentage=int(input())
else:
    print("Valor no es valido")    



    


    
        
#print("¿Que porcentaje de descuento tiene el producto?\n Digita un valor de 0 a 100\n Si el producto no tiene descuento digita el valor 0 ")
#discountPercentage=int(input())
