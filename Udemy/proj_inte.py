def num_validation(entrada):
    try:
        num = int(entrada)
        return True, num
    except:
        return False,'O valor inserido não é um número.'
    
def bi_validation(numero):

    tupla_numero = tuple(numero)

    for i in tupla_numero:
        if int(i)>1:
            return False, 'O número inserido não era bínario.'
        else:
            continue
    return True, tupla_numero

def calculo(entrada,quant):
    resultado = 0
    tupla_entrada = bi_validation(entrada)[1]

    for ind, i in enumerate(range((quant-1),-1,-1)):
        resultado += int(tupla_entrada[ind])*(2**(i))
    return f'O número {entrada} é igual a {resultado}'

def oct_validation(numero):
    tupla_numero = tuple(numero)

    for i in tupla_numero:
        if int(i)>7:
            return False, 'O número inserido não é Octal.'
        else:
            continue
    return True, tupla_numero

def calculo_oct(entrada,quant):
    resultado = 0
    tupla_entrada = oct_validation(entrada)[1]

    for ind, i in enumerate(range((quant-1),-1,-1)):
        resultado += int(tupla_entrada[ind])*(8**(i))
    return f'O número {entrada} é igual a {resultado}'
    
def hex_validation(numero):
    lista_numero = list(numero)
    for ind ,i in enumerate(lista_numero):
        if i == 'a' or i == 'A':
            lista_numero[ind] = 10
        elif i == 'b' or i == 'B':
            lista_numero[ind] = 11
        elif i == 'c' or i == 'C':
            lista_numero[ind] = 12
        elif i == 'd' or i == 'D':
            lista_numero[ind] = 13
        elif i == 'e' or i == 'e':
            lista_numero[ind] = 14
        elif i == 'f' or i == 'F':
            lista_numero[ind] = 15
            
    for i in lista_numero:
        if int(i)>15:
            return False, 'O número inserido não era hexadecimal.'
        else:
            continue
    return True, lista_numero

def hex_calculo(entrada,quant):
    resultado = 0
    tupla_entrada = hex_validation(entrada)[1]

    for ind, i in enumerate(range((quant-1),-1,-1)):
        resultado += int(tupla_entrada[ind])*(16**(i))
    return f'O número {entrada} é igual a {resultado}'


print(f"""{20*'-'}
Calculado de BINARIO, OCTAL E HEXADECIMAL PARA DECIMAL
{20*'-'}
BINARIO (PRESS '1'), OCTAL (PRESS '2'), HEXADECIMAL (PRESS '3')""")
opcao = input('R:')

def binario():
    while True:
        entrada = input('Digite um numero BINARIO:')
        if num_validation(entrada):
            quant = len(entrada)

            if bi_validation(entrada)[0]:
                print(calculo(entrada,quant))

            else:
                print(bi_validation(entrada)[1])
                continue

            break
        else:
            print(num_validation(entrada)[1])

            continue
        
def octal():
    while True:
        entrada = input('Digite um numero em OCTAL:')
        if num_validation(entrada):
            quant = len(entrada)

            if oct_validation(entrada)[0]:
                print(calculo_oct(entrada,quant))

            else:
                print(oct_validation(entrada)[1])
                continue

            break
        else:
            print(num_validation(entrada)[1])

            continue
        
def hexa():
    while True:
        entrada = input('Digite um numero em OCTAL:')
        if True:
            quant = len(entrada)

            if hex_validation(entrada)[0]:
                print(hex_calculo(entrada,quant))

            else:
                print(hex_validation(entrada)[1])
                continue

            break
        
             
if opcao == '1':
    binario()
elif opcao == '2':
    octal()
elif opcao == '3':
    hexa()