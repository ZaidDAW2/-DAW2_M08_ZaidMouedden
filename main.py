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
    case 1:
        binario = input("Introduce el numero en binario: ")
        print(conversor.binario_decimal(binario))

    case 2:
        decimal = input("Introduce el numero en decimal: ")
        print(conversor.decimal_binario(decimal))
        

