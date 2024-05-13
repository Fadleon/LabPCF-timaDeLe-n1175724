print("Proyecto licuados")
nombrecliente = input("Ingrese su nombre: ")
NIT = input("Ingrese su NIT (si no tienes pon cf): ")
print("Nuestro licuado por defecto es el licuado de fresa con leche deslactosada sin azucar y tamaño normal")

# Variables independientes a lo que mi compa el cliente diga
preciolicuadobase = 20
cantidad_azucar = 0
tipo_leche = "deslactosada"
precio_leche = 0
agrandado = False

while True:  # Bucle para el menú de los deliciosos licuados de fresa
 
    print("\nAcciones que se pueden realizar:")
    print("1. Ver información del pedido")
    print("2. Agregar azúcar")
    print("3. Modificar leche")
    print("4. Agrandar")
    print("5. Confirmar")
    fatima = int(input("Que modificacion o accion quieres hacer querido cliente: "))
    # jajaja soy yo
    match fatima:
        case 1:
            print("Nombre del cliente:", nombrecliente)
            print("NIT:", NIT)
            print("Licuado: Fresa con leche", tipo_leche, "y", cantidad_azucar, "cucharadas de azúcar")
            print("Tamaño:", "Grande" if agrandado else "Normal")
            precio_final = preciolicuadobase + precio_leche + cantidad_azucar * 0.50
            print("Precio:", precio_final)
        
        case 2:

            if cantidad_azucar >= 2:
                print("No podemos agregar mas de 2 cucharadas de azucar porque nos importa tu salud ;)")
            else:
                cantidad_azucar += 1
                print("Se ha agregado una cucharada de azúcar.")
        
        case 3:
            print("Tipos de leche:")
            print("1. Sin leche (descuento de Q2.00)")
            print("2. Deslactosada (sin cambios en el precio)")
            print("3. Leche entera (sin cambios en el precio)")
            print("4. Leche de soya (aumento de Q3.00)")
            suji = int(input("Seleccione el tipo de leche: "))
            
            match suji:
                case 1:
                    precio_leche = -2
                    tipo_leche = "sin leche"
                case 2:
                    precio_leche = +0
                    tipo_leche = "deslactosada"
                case 3:
                    precio_leche = +0
                    tipo_leche = "entera"
                case 4:
                    precio_leche = 3
                    tipo_leche = "de soya"
                case _:
                    print("Bro no tenemos otro tipo de leche solo las que ya te dije")
        
        case 4:
            if not agrandado:
                preciolicuadobase *= 1.05
                agrandado = True
                print("Se ha agrandado el licuado.")
            else:
                print("El licuado ya ha sido agrandado una vez.")
    
        case 5:
            print("Pedido confirmado. ¡Gracias por su compra!")
            precio_final = preciolicuadobase + precio_leche + cantidad_azucar * 0.50
            print("Precio final del pedido:", precio_final)
            break
        
        case _:
            print("Estimadisimo cliente por favor elegir una de las opciones QUE SI TE DIJE")