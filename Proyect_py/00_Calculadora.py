 ## Realizar una calculadora que realice las siguientes operaciones: ##
'''
# Suma ,# Resta, Multiplicación, División, Potencia, Raíz Cuadrada, Factorial
# Módulo, División Entera, Logaritmo Natural, Logaritmo en Base10, Logaritmo en Base 2
# y Exponencial.    
'''

#### Todas las operaciones seran divididas en modulos para cada funcion de operacion que se vaya a realizar ####
## Todas las operaciones que se vayan a desplegar sean en un menu interactivo con el usuario ##
'''
El menu debe contener un titulo inovador y que de una bienvenida asi como una breve entrada al programa.
'''
##########################  Despliegue de librerias #######################################
import math
###########################################################################################
###########################     Funcion del menu.   #######################################
def show_menu():
    print("#########################################")
    print("             Calculator (Pylac)          ")
    print("#########################################")
    print("Bienvenido al programa, ¿qué operación quieres realizar?")
    print("1. Suma.")
    print("2. Resta.")
    print("3. Multiplicacion.")
    print("4. Division.")
    print("5. Potencia.")
    print("6. Raiz (n)")
    print("7. Factorial.")
    print("8. Modulo.")
    print("9. Division Entera.")
    print("10. Logaritmo Natural.")
    print("11. Logaritmo en Base10.")
    print("12. Logaritmo en Base2.")
    print("13. Exponencial.")
    print("14. Saliendo del programa.")
    print("#########################################")
############################################################################################################
    while True:
        try:
            opcion = int(input("Elige alguna opcion del 1-14: "))
            if 1 <= opcion <= 14:
                return opcion
            else:
                print("Por favor ingresa un número entre 1 y 14.")
        except ValueError:
            print("Entrada inválida. Debes ingresar un número entero.")
#############################################################################################################
def suma():
    n = int(input("¿Cuántos números deseas sumar? "))
    resultado = 0
    for i in range(n):
        numero = float(input(f"Ingresa el número {i+1}: "))
        resultado += numero    
    print(f"El resultado de la suma es: {resultado}")
    return resultado

def resta():
    n = int(input("¿Cuántos números deseas restar? "))
    resultado = 0
    for i in range(n):
        if i == 0:
            numero = float(input("Ingrese el primer número a restar: "))
            resultado = numero
        else:
            numero = float(input(f"Ingrese el número {i+1} a restar: "))
            resultado -= numero 
    print(f"El resultado de la resta es: {resultado}")
    return resultado

def division():
    n = int(input("¿Cuántos números deseas dividir? "))
    if n < 2:
        print("Debes ingresar por lo menos dos números para realizar una división.")
        return None
    
    resultado = float(input("Ingrese el primer número (dividiendo): "))
    
    for i in range(1, n):
        divisor = float(input(f"Ingrese el divisor número {i+1}: "))
        
        if divisor == 0:
            print("Error: No se puede dividir entre cero (Indeterminación).")
            return None 
        
        resultado /= divisor

    print(f"El resultado de la división es: {resultado}")
    return resultado

def multiplicacion():
    n = int(input("¿Cuántos números quieres multiplicar? "))
    if n < 2:
        print("Debes ingresar al menos dos números.")
        return None
    
    resultado = float(input("Ingresa el número 1 a multiplicar: "))
    for i in range(1, n):
        numero = float(input(f"Ingresa el número {i+1} a multiplicar: "))
        resultado *= numero 
    
    print(f"El producto es: {resultado}")
    return resultado

def potencia():
    n1 = float(input("Ingresa el coeficiente: "))
    n2 = float(input("Ingresa el exponente al que quieres elevar el coeficiente: "))
    resultado = math.pow(n1, n2)
    print(f"El resultado de la potencia es: {resultado}")
    return resultado

def calcular_raiz(radicando, indice=2, coeficiente=1):
    if radicando < 0 and indice % 2 == 0:
        return "Error: No se puede calcular la raíz par de un número negativo en los reales."
    raiz = radicando ** (1 / indice)
    resultado = coeficiente * raiz
    return resultado

def raiz_interactiva():
    radicando = float(input("Ingresa el número: "))
    indice_input = input("Ingresa el índice de la raíz (por defecto 2): ")
    indice = int(indice_input) if indice_input else 2
    if indice == 0:
        print("Error: El índice de la raíz no puede ser cero.")
        return None
    
    coef_input = input("Ingresa el coeficiente (opcional, presiona Enter para 1): ")
    coeficiente = float(coef_input) if coef_input else 1
    
    resultado = calcular_raiz(radicando, indice, coeficiente)
    print(f"El resultado es: {resultado}")
    return resultado

def modulo():
    a = float(input("Ingresa el dividendo: "))
    b = float(input("Ingresa el divisor: "))
    if b == 0:
        print("Error: División entre cero no permitida.")
        return None
    resultado = a % b
    print(f"El resultado del módulo es: {resultado}")
    return resultado

def division_entera():
    a = int(input("Ingresa el dividendo entero: "))
    b = int(input("Ingresa el divisor entero: "))
    if b == 0:
        print("Error: División entre cero no permitida.")
        return None
    resultado = a // b
    print(f"El resultado de la división entera es: {resultado}")
    return resultado

def factorial():
    n = int(input("Ingresa un número entero no negativo para calcular su factorial: "))
    if n < 0:
        print("Error: No se puede calcular el factorial de un número negativo.")
        return None
    resultado = math.factorial(n)
    print(f"El factorial de {n} es: {resultado}")
    return resultado

def logaritmo_natural():
    x = float(input("Ingresa el número positivo para calcular logaritmo natural: "))
    if x <= 0:
        print("Error: El número debe ser mayor que cero.")
        return None
    resultado = math.log(x)
    print(f"El logaritmo natural de {x} es: {resultado}")
    return resultado

def logaritmo_base_10():
    x = float(input("Ingresa el número positivo para calcular logaritmo base 10: "))
    if x <= 0:
        print("Error: El número debe ser mayor que cero.")
        return None
    resultado = math.log10(x)
    print(f"El logaritmo base 10 de {x} es: {resultado}")
    return resultado

def logaritmo_base_2():
    x = float(input("Ingresa el número positivo para calcular logaritmo base 2: "))
    if x <= 0:
        print("Error: El número debe ser mayor que cero.")
        return None
    resultado = math.log2(x)
    print(f"El logaritmo base 2 de {x} es: {resultado}")
    return resultado

def exponencial():
    x = float(input("Ingresa el exponente para calcular e^x: "))
    resultado = math.exp(x)
    print(f"El exponencial de {x} es: {resultado}")
    return resultado

def main():
    while True:
        opcion = show_menu()
        match opcion:
            case 1:
                print("######   Suma    ######")
                suma()
                print("#############################")
            case 2:
                print("######   Resta   ######")
                resta()
                print("#############################")
            case 3:
                print("######   Multiplicacion  ######")
                multiplicacion()
                print("#############################")
            case 4:
                print("######   Division   ######")
                division()
                print("#############################")
            case 5:
                print("######   Potencia    ######")
                potencia()
                print("#############################")
            case 6:
                print("######   Raiz Cuadrada   ######")
                raiz_interactiva()
                print("#############################")
            case 7:
                print("######   Factorial   ######")
                factorial()
                print("#############################")
            case 8:
                print("######   Módulo   ######")
                modulo()
                print("#############################")
            case 9:
                print("######   División Entera   ######")
                division_entera()
                print("#############################")
            case 10:
                print("######   Logaritmo Natural   ######")
                logaritmo_natural()
                print("#############################")
            case 11:
                print("######   Logaritmo en Base10   ######")
                logaritmo_base_10()
                print("#############################")
            case 12:
                print("######   Logaritmo en Base2   ######")
                logaritmo_base_2()
                print("#############################")
            case 13:
                print("######   Exponencial   ######")
                exponencial()
                print("#############################")
            case 14:
                print("Saliendo del programa.")
                break
            case _:
                print("Selección inválida... Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
