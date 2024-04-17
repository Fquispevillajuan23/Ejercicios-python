import math

# Definir la función para convertir ángulos
def convertir_angulo(angulo, unidad):
    if unidad == "grados":
        angulo_radianes = angulo * (math.pi / 180)
        return angulo_radianes
    elif unidad == "radianes":
        angulo_grados = angulo * (180 / math.pi)
        return angulo_grados
    else:
        return "Unidad de medida no válida"

# Inicio del programa
def main():
    # Pedir al usuario que ingrese el ángulo y la unidad de medida
    angulo = float(input("Ingrese el ángulo: "))
    unidad = input("Ingrese la unidad de medida (grados o radianes): ").lower()

    # Convertir el ángulo llamando a la función convertir_angulo
    resultado = convertir_angulo(angulo, unidad)

    # Mostrar el resultado al usuario
    if isinstance(resultado, str):
        print(resultado)
    else:
        print("El ángulo convertido es:", resultado)

# Llamar a la función main para ejecutar el programa
if __name__ == "__main__":
    main()