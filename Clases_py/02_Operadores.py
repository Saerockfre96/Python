#Operadores en Python

print("Operadores en Python - Ejemplos")
###Operadores Aritmeticos###
print (3+4) #suma
print (3-4) #resta
print (3*4) #multiplicacion
print (3/4) #division
print (3//4) #division entera
print (3**4) #potencia
print (3%4) #modulo

'''
Nota: No podemos juntar operadores aritmeticos con tipos de datos diferentes es decir string 
y enteros, por ejemplo:
mas enteros o usar operadores aritmeticos en la concatenacion de strings
'''

# Podemos concatenar strings y números convirtiendo el número a string
print('Hola ' + str(5))
print('Hola' * 5)
#Tmbien se puede hacer 
my_float = 2.5 * 2
print ( 'hola' * int (my_float) ) #Convierte el float a int y multiplica la cadena por 5

### Operadores de Comparacion ###
print(3 == 4) #igual
print(3 != 4) #diferente        
print(3 > 4)  #mayor que
print(3 < 4)  #menor que
print(3 >= 4) #mayor o igual que
print(3 <= 4) #menor o igual que

### Operadores Logicos ###
print(3 == 4 and 5 > 2) #and
print(3 < 4 or 5 > 2)  #or
print(not(3 == 4))       #not   
