   

def case1 ():
    return 3+2

def case2 ():
    return 3-1

def case3 ():
    return 5*2
    
def default_case ():
    return "salir del programa"   
   
def switch_case (argument):
        switcher = {
            1: case1,
            2: case2,
            3: case3,
        }
        #obtener la funcion de la calculadora
        func = switcher. get (argument, default_case)
        #llamar a la funcion 
        return func()
    # Ejemplo de uso
opcion = input()
entero=int(opcion)
print(switch_case(entero))