entrada = input('Digite um numero INTEIRO que deseja ter o resultado em fatorial: ')
num_int = int(entrada)
resultado = 1
for i in range(1,num_int+1):
    resultado *= i

print(resultado)