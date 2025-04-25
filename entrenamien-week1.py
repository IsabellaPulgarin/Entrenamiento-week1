

# Pedirle el numbre del producto al usuario y guardarlo en una variable
print("Ingresa el nombre del producto")
nameProduct=input() 

# Pedirle al usuario el precio del producto
print("Ingrese el precio unitario del producto")
productPrice=float(input())

# El numero ingresado sea positivo para seguir ejecutando el programa de lo contrario arroje: (valor no valido)
if productPrice>0:
    print("Ingresa la cantidad del producto adquirido")
    quantityProducts=int(input())
    if quantityProducts>0:
        print("¿El producto tiene descuento?\nRespone:\n1=si\n2=no")     # Le di valor a las respuestas 
        ask=int(input())
        
        # Aca puse 2 condiciones 1 para el si y 2 para el no, de lo contrario arroje: (valor no valido)
        if ask==1:
            print("¿Que porcentaje de descuento tiene el producto?\nDigita un valor de 1 a 100")
            discountPercentage=int(input())
            
            # El valor ingresado debe de ser de 1 a 100 para seguir de lo contrario arroje: (valor no valido)
            if discountPercentage>=1 and discountPercentage<100:   
                print("Excelente")
                print(f"El producto es: {nameProduct}\nSu precio es: {productPrice:.2f}\nLlevara {quantityProducts} {nameProduct}\nEl descuento es de: {discountPercentage}\nCosto total sin descuento: {"%.2f"%(productPrice*quantityProducts)}\nCosto total con descuento: {"%.2f"%((productPrice*quantityProducts)*(discountPercentage/100))}")
            else:
                print("Valor no valido")
        elif ask==2:
            print("Si el producto no tiene descuento digita el valor 0")  
            discountPercentage=int(input())
            
            # El valor que ingrese el usuario tiene que ser 0 de lo contrario arroje: (valor no valido)
            if discountPercentage==0:
                print("Es correcto")
                print(f"El producto es: {nameProduct}\nSu precio es: {productPrice:.2f}\nLlevara {quantityProducts} {nameProduct}\nEl descuento es de: {discountPercentage}\nCosto total sin descuento: {"%.2f"%(productPrice*quantityProducts)}\nCosto total con descuento: {"%.2f"%((productPrice*quantityProducts)*(discountPercentage/100))}")
            else:
                print("Valor no valido")
        else:
            print("Valor no valido")  
                
    else:
        print("Valor no valido")   
else:
    print("Valor no valido")
