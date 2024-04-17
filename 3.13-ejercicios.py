# Definir la función para asignar la calificación literal
def asignar_calificacion_literal(calificacion_numerica):
    if calificacion_numerica >= 9.1:
        calificacion_literal = "A Excelente"
    elif calificacion_numerica >= 8.1:
        calificacion_literal = "B Muy bien"
    elif calificacion_numerica >= 7.5:
        calificacion_literal = "C Bien"
    else:
        calificacion_literal = "R Reprobado"
    return calificacion_literal

# Inicio del programa
def main():
    # Pedir al usuario que ingrese la calificación numérica
    calificacion_numerica = float(input("Ingrese la calificación numérica: "))

    # Asignar la calificación literal llamando a la función asignar_calificacion_literal
    calificacion_literal = asignar_calificacion_literal(calificacion_numerica)

    # Mostrar la calificación literal al usuario
    print("La calificación literal es:", calificacion_literal)