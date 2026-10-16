import math

listado_binario = []
numero_decimal = 0

def decimal_binario_entero(decimal):
    while decimal/2!=0:
        listado_binario.append(int(decimal%2))
        decimal = int(decimal/2)
    listado_binario.reverse()

    return listado_binario

def decimal_binario_con_decimales(decimal):

    parte_decimal,parte_entera = math.modf(decimal)
    listado_binario.append(".")
    while parte_entera/2!=0:
        listado_binario.append(int(parte_entera%2))
        parte_entera = int(parte_entera/2)
    listado_binario.reverse()

    restante = 0.0
    iteraciones_maximas = 10
    vueltas = 1

    while restante != 1.0 and vueltas<=iteraciones_maximas:
        resultado_temporal = parte_decimal * 2
        restante,bit = math.modf(resultado_temporal)
        listado_binario.append(int(bit))
        vueltas +=1

    return listado_binario

