entrada = input('Digite a operação que deseja fazer: Ex:(10+4) * digite somente dois digitos R:')
if '+' in entrada:
    n1, n2 = entrada.replace(' ','').split('+')
    n1_float, n2_float = float(n1),float(n2)
    resultado = n1_float + n2_float
elif '-' in entrada:
    n1, n2 = entrada.replace(' ','').split('-')
    n1_float, n2_float = float(n1),float(n2)
    resultado = n1_float - n2_float
elif '*' in entrada:
    n1, n2 = entrada.replace(' ','').split('*')
    n1_float, n2_float = float(n1),float(n2)
    resultado = n1_float * n2_float
elif '/' in entrada:
    n1, n2 = entrada.replace(' ','').split('/')
    n1_float, n2_float = float(n1),float(n2)
    resultado = n1_float / n2_float
print(f'O resultado da conta é {resultado}')