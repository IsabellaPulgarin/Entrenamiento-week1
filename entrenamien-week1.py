print("Ingresa el nombre del producto")
nameProduct=input()
if type(nameProduct) == str:
    print("Ingrese el precio unitario del producto")
    productPrice=float(input())
    if productPrice>0:
        print("Ingresa la cantidad del producto adquirido")
        quantityProducts=int(input())
        if quantityProducts>0:
            print("¿El producto tiene descuento?\nRespone:\n1=si\n2=no")
            ask=int(input())
            if ask==1:
                print("¿Que porcentaje de descuento tiene el producto?\nDigita un valor de 1 a 100")
                discountPercentage=int(input())
                if discountPercentage>=1 and discountPercentage<100:
                    print("Excelente")
                    print(f"El producto es: {nameProduct}\nSu precio es: {productPrice}\nLlevara {quantityProducts} {nameProduct}\nEl descuento es de: {discountPercentage}\nCosto total sin descuento: {productPrice*quantityProducts}\nCosto total con descuento: {(productPrice*quantityProducts)*(discountPercentage/100)}")
                else:
                    print("Valor no valido")
            elif ask==2:
                print("Si el producto no tiene descuento digita el valor 0")  
                discountPercentage=int(input())
                if discountPercentage==0:
                    print("Es correcto")
                    print(f"El producto es: {nameProduct}\nSu precio es: {productPrice}\nLlevara {quantityProducts} {nameProduct}\nEl descuento es de: {discountPercentage}\nCosto total sin descuento: {productPrice*quantityProducts}\nCosto total con descuento: {(productPrice*quantityProducts)*(discountPercentage/100)}")
                else:
                    print("Valor no valido")
            else:
                print("Valor no valido")  
                
        else:
            print("Valor no valido")   
    else:
        print("Valor no valido")
else:
    print("valor no valido")