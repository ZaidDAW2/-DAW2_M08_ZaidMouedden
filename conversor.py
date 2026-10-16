import math

listado_binario = []
numero_decimal = 0

def decimal_binario(decimal):
    if "." in decimal:

        decimal = float(decimal)
        parte_decimal,parte_entera = math.modf(decimal)

        while parte_entera/2!=0:
            listado_binario.append(int(parte_entera%2))
            parte_entera = int(parte_entera/2)
        listado_binario.reverse()
        
        restante = 0.0
        iteraciones_maximas = 10
        vueltas = 1
        
        listado_binario.append(".")
        while restante != 1.0 and vueltas<=iteraciones_maximas:
            resultado_temporal = parte_decimal * 2
            restante,bit = math.modf(resultado_temporal)
            listado_binario.append(int(bit))
            vueltas +=1
        
            return listado_binario
        
    else:
        decimal = int(decimal)
        
    while decimal/2!=0:
        listado_binario.append(int(decimal%2))
        decimal = int(decimal/2)
    listado_binario.reverse()

    return listado_binario

def binario_decimal(binario):
    suma_total = 0
    valor = 0
    
    for i,digito in enumerate(reversed(str(binario))):
        valor = 2**i
        suma_total += int(digito)*valor
        print(digito,suma_total,valor,sep=" // ")

    return suma_total