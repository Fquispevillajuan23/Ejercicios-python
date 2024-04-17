# Definir la función para calcular el interés y el saldo final
def calcular_saldo_final(saldo):
    if saldo < 10000.00:
        interes = saldo * 0.03
        saldo_final = saldo + interes
    else:
        interes = saldo * 0.04
        saldo_final = saldo + interes
    return saldo_final


# Inicio del programa
def main():
    # Pedir al usuario que ingrese el saldo
    saldo = float(input("Ingrese el saldo de la cuenta: $"))

    # Calcular el saldo final llamando a la función calcular_saldo_final
    saldo_final = calcular_saldo_final(saldo)

    # Mostrar el saldo final al usuario
    print("El saldo final después de un año es: ${:.2f}".format(saldo_final))


# Llamar a la función main para ejecutar el programa
if __name__ == "__main__":
    main()