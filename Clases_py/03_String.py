### String ###
##Maneras de utilizar las formas de los strings en manera estetica###
'''
\n - Salto de linea.
\t - Tabulacion.
'''
my_string = "My String"
my_other_string = 'Mi otro String'
print(len(my_string))
print(len(my_other_string))

print(my_other_string," "+ my_string)

my_new_line_string = 'Este es un string \ncon salto de linea.'
print(my_new_line_string)

my_tab_string = '\tEstes es un string con tabulacion.'
print(my_tab_string)

my_scape_line = "\tEsta es un string con \n escapado."
print(my_scape_line)

### FORMATEO ###
name , surname , age = "Samuel" , 'Moured' , 19

print("Mi nomnbre es %s %s y mi edad es %d".format(name , surname , age))
print("Mi nombre es %s %s y mi edad es %d anos" %(name , surname , age))

## Formateo profesional ##
print(f"Mi nombre es {name} {surname} y tengo {age} anos")

## Desempaquetado de caracteres ##
language = "python"
a , b , c , d , e , f = language
print (a)
print (e)

## Division 
language_slice = language [-1]
print(language_slice)

language_slice = language [0:3:4]
print(language_slice)
#Reves 
reversed_language = language[ ::-1]
print(reversed_language)

# Funciones del sistema.
print(language.capitalize())
print(language.upper())
print(language.count("o"))
print(language.lower().isupper())
print(language.upper().isupper())
print(language.startswith("py"))
print( "Py" == "Py")