entrada = input('Digite um numero para definir o intervalo de numeros pares: ')
entrada2 = input('Digite um numero para definir o intervalo de numeros pares: ')
num_int = int(entrada)
num_int2 = int(entrada2)
resultado = []
for i in range(num_int+1,num_int2):
    if i%2==0:
        resultado.append(i)

print(f'Existem {resultado} dentro de {num_int} e {num_int2}')
