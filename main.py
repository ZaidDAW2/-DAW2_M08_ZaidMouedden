import conversor as conversor

print(
    "Que conversion quiere realizar?",
    "1.Binario a decimal",
    "2.Decimal a Binario",
    "3.Octal a binario",
    "4.Binario a octal",
    "5.Hex a binario",
    "6.Binario a Hex",
    sep="\n")

numero = int(input("Introduzca un numero: "))
print("========================================")
match numero: 
    case 2:
        decimal = input("Introduce el numero en decimal: ")

        if "." in decimal:
            decimal = float(decimal)
            print(conversor.decimal_binario_con_decimales(decimal))
        else:
            decimal = int(decimal)
            print(conversor.decimal_binario_entero(decimal))

