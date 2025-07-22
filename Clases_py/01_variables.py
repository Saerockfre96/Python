# Variables 
#Prueba 1 . Creacion de variables de tipo string.
Myvariable = 'My String Variable'
print(Myvariable)
# Prueba 2. Creacion de variables de tipo string.
my_string_variable = "My String Variable"
print(my_string_variable)
# Prueba 3. Variables enteras.
my_int_variable =10
print("My integer variable is:",my_int_variable)
# Prueba 4. Boolean variables.
my_bool_variable = True
print("My boolean variable is:", my_bool_variable)
# Prueba 5. Conjuntos de variables.
skills = {"Python", "Java", "C++"}
print("My skills are:", skills)
# Prueba 6. Concatenacion de variables.
print (my_bool_variable, my_int_variable, my_string_variable, skills)
# Prueba 7. Longitud de una variable string.
'''
Calcula la longitud de la variable my_string_variable contando los caracteres y espacios.
'''
print("Declaracion de funcion para calcular la longitud de una variable tipo string:Len()")
print(len(my_string_variable))
#Prueba 8. Longitud de una variable tipo conjunto.
'''
Calcula la longitud de la variable skills contando los elementos del conjunto.
'''
print("Declaracion de funcion para calcular la longitud de una variable tipo conjunto: Len()")
print(len(skills))

#Variables de una sola linea. Cuidado con abusar de esta sintaxis.
# Prueba 9. Variables de una sola linea.
name , surname , alias , edad = "Samuel", "Ibarra" , "Sam" , 19
print("My name is:", name , "my surname is : " , surname , "my alias is: " , alias , "and my age is : " , edad )

#Uso de variables con input.
# Prueba 10. Uso de variables con input.
name = input("Enter your name: ")
surname = input("Enter your surname: ")
print(len(name))
print(type(name))

