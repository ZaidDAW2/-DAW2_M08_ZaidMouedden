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

def binario_octal(binario):

    numero = ""
    if len(binario)%3 == 0:

        grupos = (len(binario)//3)
        binario = binario[::-1]

        for grupo in range(grupos):

            indice = (grupo*3)-1
            tercero = int(binario[indice])
            segundo = int(binario[indice-1])
            primero = int(binario[indice-2])

            valor = tercero*4 + segundo*2 + primero*1

            numero+=str(valor)
        
    else:
        grupos = (len(binario)//3)
        binario = binario[::-1]

        for grupo in range(grupos+1):

            indice = (grupo*3)-1
            revision_vacios = binario[indice-2:indice:3]
            hay_hueco = True if len(revision_vacios)<3 else False

            if hay_hueco:
                #Hay que saber cuantos huecos hay para rellenarlos con 0s

                huecos = 3-len(revision_vacios)
                restantes = abs(len(revision_vacios)-3)

                for restante in range(restantes):
                    indice_restantes = indice-restante
                    valor = int(binario[indice_restantes])
                    numero+=str(valor*(2**restante-1))

                for hueco in range(huecos):
                    valor_hueco = binario[indice-hueco]="0"
                    numero+=valor_hueco

            else:
                tercero = int(binario[indice])
                segundo = int(binario[indice-1])
                primero = int(binario[indice-2])

            valor = tercero*4 + segundo*2 + primero*1

            numero+=str(valor)
    return numero







