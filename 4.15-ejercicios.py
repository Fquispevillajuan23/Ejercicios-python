# Paso 1: Leer el número de caracteres de cada lado (N)
N = int(input("Ingrese el número de caracteres de cada lado del cuadrado: "))

# Paso 2: Escribir el borde superior del cuadrado
print("_" * N)

# Paso 3: Escribir los lados laterales y el espacio en blanco en el centro
for i in range(N - 2):
    print("|" + " " * (N - 2) + "|")

# Paso 4: Escribir el borde inferior del cuadrado
print("_" * N)