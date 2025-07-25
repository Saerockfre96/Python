def numeracion_opcional():
    n = int(input("¿Hasta qué número quieres hacer la enumeración?: "))
    for i in range(n+1):
        print(i)

def main():
    numeracion_opcional()

main()
